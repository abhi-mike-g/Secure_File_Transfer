from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import time
from utils import *

def generate_rsa_keys():
    start = time.time()
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    end = time.time()

    public_key = private_key.public_key()
    return private_key, public_key, end - start

def rsa_encrypt_key(aes_key, public_key):
    start = time.time()
    encrypted_key = public_key.encrypt(
        aes_key,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(), label=None)
    )
    end = time.time()
    return encrypted_key, end - start

def rsa_decrypt_key(encrypted_key, private_key):
    start = time.time()
    key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(), label=None)
    )
    end = time.time()
    return key, end - start

def test_rsa(file_path):
    print(f"\n📄 Testing RSA with file: {file_path}")
    private_key, public_key, keygen_time = generate_rsa_keys()
    aes_key = generate_aes_key()

    enc_key, enc_key_time = rsa_encrypt_key(aes_key, public_key)
    dec_key, dec_key_time = rsa_decrypt_key(enc_key, private_key)

    assert aes_key == dec_key, "Decryption failed"

    start = time.time()
    aes_encrypt_file(file_path, "rsa_encrypted.bin", aes_key)
    enc_time = time.time() - start

    start = time.time()
    aes_decrypt_file("rsa_encrypted.bin", "rsa_decrypted.txt", aes_key)
    dec_time = time.time() - start

    print(f"🗝  Key Gen Time: {keygen_time:.4f}s")
    print(f"🔐 AES Key Encrypted in: {enc_key_time:.4f}s")
    print(f"🔓 AES Key Decrypted in: {dec_key_time:.4f}s")
    print(f"📥 File Encrypted in: {enc_time:.4f}s")
    print(f"📤 File Decrypted in: {dec_time:.4f}s")
