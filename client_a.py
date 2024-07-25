import socket
import threading
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dh

# Generate Diffie-Hellman parameters
def generate_parameters():
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    return parameters

def generate_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def load_public_key(public_key_bytes):
    return serialization.load_pem_public_key(public_key_bytes, backend=default_backend())

def encrypt_message(message, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    pad_length = 16 - (len(message) % 16)
    message += bytes([pad_length]) * pad_length
    return encryptor.update(message) + encryptor.finalize()

def decrypt_message(encrypted_message, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()
    pad_length = decrypted_message[-1]
    return decrypted_message[:-pad_length]

def receive_messages(sock, key):
    while True:
        encrypted_message, _ = sock.recvfrom(1024)
        decrypted_message = decrypt_message(encrypted_message, key)
        print("Received Message:", decrypted_message.decode('utf-8'))

def send_messages(sock, key):
    while True:
        message = input("Enter your message: ")
        encrypted_message = encrypt_message(message.encode('utf-8'), key)
        # Send the message to Client B
        sock.sendto(encrypted_message, (B_IP, B_PORT))

# Client A settings
A_IP = '1.2.3.4'
A_PORT = 1234
B_IP = '1.2.3.5'
B_PORT = 1235

parameters = generate_parameters()
private_key_a, public_key_a = generate_key_pair(parameters)

# Send public key to Client B
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((A_IP, A_PORT))
print("Client A is waiting for Client B to connect...")

sock.sendto(public_key_a.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
), (B_IP, B_PORT))

# Receive public key from Client B
public_key_b_bytes, _ = sock.recvfrom(1024)
public_key_b = load_public_key(public_key_b_bytes)

# Compute the shared key
shared_key = private_key_a.exchange(public_key_b)
key = shared_key[:16]  # AES key size must be 16 bytes

print("Key exchange completed. You are ready to send messages.")

# Create threads for receiving and sending messages
receive_thread = threading.Thread(target=receive_messages, args=(sock, key))
send_thread = threading.Thread(target=send_messages, args=(sock, key))

receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()
