from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
import time
from utils import *

def generate_ecc_keys():
    start = time.time()
    private_key = ec.generate_private_key(ec.SECP256R1())
    end = time.time()
    public_key = private_key.public_key()
    return private_key, public_key, end - start

def derive_shared_key(priv_key, peer_pub_key):
    shared_secret = priv_key.exchange(ec.ECDH(), peer_pub_key)
    return HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'ecdh',
    ).derive(shared_secret)

def test_ecc(file_path):
    print(f"\n📄 Testing ECC with file: {file_path}")
    priv_a, pub_a, keygen_time = generate_ecc_keys()
    priv_b, pub_b, _ = generate_ecc_keys()

    start = time.time()
    shared_key_sender = derive_shared_key(priv_a, pub_b)
    enc_key_time = time.time() - start

    start = time.time()
    shared_key_receiver = derive_shared_key(priv_b, pub_a)
    dec_key_time = time.time() - start

    assert shared_key_sender == shared_key_receiver, "Key exchange mismatch"

    start = time.time()
    aes_encrypt_file(file_path, "ecc_encrypted.bin", shared_key_sender)
    enc_time = time.time() - start

    start = time.time()
    aes_decrypt_file("ecc_encrypted.bin", "ecc_decrypted.txt", shared_key_receiver)
    dec_time = time.time() - start

    print(f"🗝  Key Gen Time: {keygen_time:.4f}s")
    print(f"🔐 Shared Key Derived in: {enc_key_time:.4f}s")
    print(f"🔓 Shared Key Derived in: {dec_key_time:.4f}s")
    print(f"📥 File Encrypted in: {enc_time:.4f}s")
    print(f"📤 File Decrypted in: {dec_time:.4f}s")
