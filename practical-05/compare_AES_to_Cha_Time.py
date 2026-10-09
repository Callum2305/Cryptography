import os
import time

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Same 10 MB message for both ciphers
plaintext_bytes = os.urandom(10000000)

# --- ChaCha20 ---
key_bytes = os.urandom(32)
nonce_bytes = bytes(4) + os.urandom(12)
chacha20_cipher = Cipher(algorithms.ChaCha20(key_bytes, nonce_bytes), mode=None)
chacha20_encryptor = chacha20_cipher.encryptor()

before = time.perf_counter()
ciphertext_bytes = chacha20_encryptor.update(plaintext_bytes) + chacha20_encryptor.finalize()
after = time.perf_counter()
print(f"ChaCha20: {after - before:0.4f} seconds")

# --- AES in Counter Mode ---
key_bytes = os.urandom(32)
nonce_bytes = os.urandom(12) + bytes(4)
aes_ctr_cipher = Cipher(algorithms.AES(key_bytes), mode=modes.CTR(nonce_bytes))
aes_ctr_encryptor = aes_ctr_cipher.encryptor()

before = time.perf_counter()
ciphertext_bytes = aes_ctr_encryptor.update(plaintext_bytes) + aes_ctr_encryptor.finalize()
after = time.perf_counter()
print(f"AES-CTR:  {after - before:0.4f} seconds")

# AES is typically faster as it is inbuilt into systems so it will be faster, but if you run it as CTR,
# it will run slower because it is not its original spec, so it goes faster.