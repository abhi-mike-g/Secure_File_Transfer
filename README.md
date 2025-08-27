# 🔒 Secure File Transfer System using RSA & ECC

## Project Overview

This project demonstrates a **secure file transfer system** leveraging modern cryptography techniques:

* **Asymmetric Encryption**: RSA-2048 and ECC (secp256r1) for **key exchange**.
* **Symmetric Encryption**: AES-256 for encrypting the actual file content.
* Designed for **performance evaluation** and **security analysis** of different key exchange mechanisms.

The system is modular, allowing easy testing of RSA and ECC workflows on different file sizes.

---

## 📦 Project Structure

```
secure_file_transfer/
│
├── rsa_transfer.py       # RSA key exchange + AES file encryption
├── ecc_transfer.py       # ECC (ECDH) key exchange + AES file encryption
├── utils.py              # AES encryption/decryption & helper functions
├── test_files/           # Sample files for testing
│   ├── file_1MB.txt
│   └── file_10MB.txt
├── main.py               # Run all tests and benchmark RSA vs ECC
└── README.md             # Project documentation
```

---

## 🔧 Requirements

Install required Python libraries:

```bash
pip install cryptography pycryptodome tqdm
```

* `cryptography` – for RSA/ECC key generation and key exchange
* `pycryptodome` – for AES encryption/decryption
* `tqdm` – optional, for progress bars in file encryption

---

## 🧠 Core Concepts

1. **AES-256 Symmetric Encryption**

   * Encrypts actual file data efficiently.
   * Keys are 32 bytes (256 bits).
   * Uses CBC mode with random IV.

2. **RSA-2048 Asymmetric Encryption**

   * Encrypts AES keys for secure transfer.
   * Public/private keys are 2048 bits (\~256 bytes).
   * Uses OAEP padding with SHA-256.

3. **ECC (secp256r1) + ECDH**

   * Efficient key exchange to derive shared AES key.
   * Smaller key size (256 bits) with comparable security.
   * Uses HKDF to derive a 32-byte AES key from ECDH shared secret.

---

## 🔐 File Encryption Flow

1. **Key Generation**

   * Generate AES-256 key for file encryption.
   * Generate RSA-2048 or ECC key pairs for key exchange.

2. **Key Exchange**

   * **RSA**: Encrypt AES key with recipient's public key.
   * **ECC**: Use ECDH to derive a shared AES key.

3. **File Encryption / Decryption**

   * AES encrypt the file in 1 MB chunks.
   * IV stored at the beginning of the encrypted file.
   * AES decrypt using same key at the receiver side.

---

## 🔧 Usage

1. Prepare sample files in `test_files/`.
2. Run `main.py` to benchmark both RSA and ECC:

```bash
python main.py
```

This will:

* Generate RSA/ECC keys
* Encrypt/decrypt AES keys
* Encrypt/decrypt files
* Measure and print performance timings

---

## 🧪 Performance Metrics

The system measures:

* **Key Generation Time**
* **AES Key Encryption / Decryption Time**
* **File Encryption / Decryption Time**

| Metric                | RSA-2048 (s) | ECC-P256 (s) |
| --------------------- | ------------ | ------------ |
| Key Generation Time   |              |              |
| Key Exchange Time     |              |              |
| 1 MB File Encryption  |              |              |
| 1 MB File Decryption  |              |              |
| 10 MB File Encryption |              |              |
| 10 MB File Decryption |              |              |

---

## ⚡ RSA vs ECC Comparison

| Feature                | RSA-2048                      | ECC (secp256r1)             |
| ---------------------- | ----------------------------- | --------------------------- |
| Key Size               | 2048 bits (256 bytes)         | 256 bits (32 bytes)         |
| Speed                  | Slower encryption/decryption  | Faster key exchange (ECDH)  |
| File Encryption        | AES-256 in both cases         | AES-256 in both cases       |
| Computational Overhead | Higher                        | Lower                       |
| Storage Requirement    | Larger keys & ciphertext      | Smaller keys & ciphertext   |
| Security (equivalent)  | \~112-bit security            | \~128-bit security          |
| Use Cases              | Legacy systems, compatibility | Modern systems, IoT, mobile |

---

## ✅ Key Takeaways

* **RSA**: Simple, compatible, but slower and resource-intensive.
* **ECC**: More efficient and secure with smaller keys; ideal for modern systems and large file transfers.
* **AES-256**: Fast symmetric encryption for actual file data.
* **Performance Evaluation**: Critical to compare key generation, exchange, and encryption speeds.

---

## 📌 Notes

* AES keys **must never be reused** across files for security.
* ECC provides **better efficiency and security** for IoT and constrained devices.
* RSA remains **widely compatible**, suitable for legacy systems.
