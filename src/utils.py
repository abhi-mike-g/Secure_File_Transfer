import os, time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from tqdm import tqdm

def generate_aes_key():
    return get_random_bytes(32)  # AES-256

def pad(data):
    padding_len = 16 - len(data) % 16
    return data + bytes([padding_len]) * padding_len

def unpad(data):
    padding_len = data[-1]
    return data[:-padding_len]

def aes_encrypt_file(in_file, out_file, key):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(in_file, 'rb') as f_in, open(out_file, 'wb') as f_out:
        f_out.write(iv)
        while chunk := f_in.read(1024 * 1024):
            chunk = pad(chunk)
            f_out.write(cipher.encrypt(chunk))

def aes_decrypt_file(in_file, out_file, key):
    with open(in_file, 'rb') as f_in:
        iv = f_in.read(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)

        with open(out_file, 'wb') as f_out:
            while chunk := f_in.read(1024 * 1024):
                decrypted = cipher.decrypt(chunk)
                f_out.write(unpad(decrypted))
