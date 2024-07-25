# English

## Project Description
This project is a simple application that provides encrypted socket communication between two clients. Communication is secured using an AES encryption algorithm with a shared key obtained through the Diffie-Hellman key exchange protocol. 
The project consists of two main components: Client A and Client B. Both clients use the Diffie-Hellman protocol to generate a shared encryption key and use this key to encrypt and decrypt messages.

## Features

- Key Exchange: Secure key exchange using the Diffie-Hellman protocol.
- Encryption: Communication secured with AES encryption.
- Client Communication: Secure messaging between clients.

## Installation and Running
Required Libraries: The libraries used in this project are:

- cryptography
- socket
- threading

You can install these libraries using the following commands:

<code>pip install cryptography</code><br>
<code>pip install socket</code><br>
<code>pip install threading</code><br>


## Running the Code:

### Client A:
Open the <code>client_a.py</code> file and configure the settings for Client A (IP address and port).
Start Client A. Initially, the key exchange will be performed, and then encrypted messages can be sent and received.

### Client B:
Open the <code>client_b.py</code> file and configure the settings for Client B (IP address and port).
Start Client B. Client B will receive the key from Client A, compute the shared key, and use it to encrypt and decrypt messages, and send new messages.

## Code Files
- <code>client_a.py</code>: Code for Client A. Generates the key, sends it to Client B, and sends encrypted messages.
- <code>client_b.py</code>: Code for Client B. Receives the key from Client A, computes the shared key, and decrypts and sends encrypted messages.

## Security Notes
The key exchange process uses the Diffie-Hellman protocol to create a shared key and ensures message security with AES encryption.
This project is a basic implementation of encryption and key exchange. Additional security measures should be considered for applications requiring higher security.

<br>
<hr>
<br>

# Türkçe

## Proje Açıklaması
Bu proje, iki istemci arasında şifreli socket iletişimi sağlayan basit bir uygulamadır. İletişim, Diffie-Hellman anahtar değişim protokolü kullanılarak sağlanan ortak bir anahtar ile AES şifrelemesiyle güvence altına alınmıştır. 
Proje iki ana bileşenden oluşur: Client A ve Client B. Her iki istemci de Diffie-Hellman protokolü kullanarak ortak bir şifreleme anahtarı oluşturur ve bu anahtar ile mesajları şifreleyip çözer.

## Özellikler

- Anahtar Değişimi: Diffie-Hellman protokolü ile güvenli anahtar değişimi.
- Şifreleme: AES algoritması kullanılarak şifrelenmiş iletişim.
- İstemci İletişimi: İstemciler arasında güvenli mesajlaşma.


## Kurulum ve Çalıştırma
Gerekli Kütüphaneler: Bu projede kullanılan kütüphaneler şunlardır:

- cryptography
- socket
- threading

Bu kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:

<code> pip install cryptography </code>
<code> pip install socket </code>
<code> pip install threading </code>

## Kodun Çalıştırılması:

### Client A:
<code>client_a.py</code> dosyasını açın ve Client A'nın ayarlarını yapın (IP adresi ve port).
Client A'yı başlatın. İlk olarak anahtar değişimi gerçekleştirilir ve ardından şifreli mesajlar gönderilebilir, gelen mesajları çözebilir.

### Client B:

<code>client_b.py</code> dosyasını açın ve Client B'nin ayarlarını yapın (IP adresi ve port).
Client B'yi başlatın. Client B, Client A'nın anahtarını alır, ortak anahtarı hesaplar ve mesajları şifreleyip çözer, yeni mesajı gönderir.

## Kod Dosyaları

- <code>client_a.py</code>: Client A'nın kodu. Anahtar oluşturur, Client B'ye gönderir ve şifreli mesajları gönderir.
- <code>client_b.py</code>: Client B'nin kodu. Client A'dan anahtar alır, ortak anahtarı hesaplar ve şifreli mesajları çözer, gönderir.


## Güvenlik Notları
Anahtar değişimi sürecinde kullanılan Diffie-Hellman protokolü, ortak anahtar oluşturulmasını sağlar ve AES şifrelemesi ile mesajların güvenliğini sağlar.
Bu proje, temel bir şifreleme ve anahtar değişim uygulamasıdır. Daha yüksek güvenlik gerektiren uygulamalarda ek güvenlik önlemleri alınmalıdır.
