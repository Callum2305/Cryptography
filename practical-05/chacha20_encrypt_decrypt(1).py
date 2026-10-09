import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

# ChaCha20 is a stream cipher (no padding needed).
# The raw API takes 16 bytes: a 4-byte little-endian block counter
# followed by a 12-byte nonce, as in RFC 7539.
# Can you decrypt without the Nonce: No, even with the key, if the nonce is off by one byte, different output.

# key_bytes = os.urandom(32)  # Fresh key for each standalone demonstration.

# For a statically set key:
key = "averylongkeymakesforaverygoodkey"
key_bytes = bytes(key, "utf-8")             # same line as always

# nonce_bytes = bytes(4) + os.urandom(12)   # random nonce generation


# Static nonce from the practical (hex, 16 bytes)
nonce_bytes = bytes.fromhex("8ec1f037a3f7322e65cf3319a73d0170")


chacha20_cipher = Cipher(algorithms.ChaCha20(key_bytes, nonce_bytes), mode=None)
# chacha20_encryptor = chacha20_cipher.encryptor() #encryption only
chacha20_decryptor = chacha20_cipher.decryptor()    # decryption only

# Encryption only:
# plaintext = "someplaintext"
# plaintext_bytes = bytes(plaintext, "utf-8")
# print("Plaintext: " + plaintext)

# ciphertext_bytes = chacha20_encryptor.update(plaintext_bytes) + chacha20_encryptor.finalize()
# ciphertext = ciphertext_bytes.hex()
# print("Ciphertext: " + ciphertext)

# plaintext_bytes_2 = chacha20_decryptor.update(ciphertext_bytes) + chacha20_decryptor.finalize()
# plaintext_2 = str(plaintext_bytes_2, "utf-8")
# print("Original Plaintext: " + plaintext_2)

# Decrupt a static set ciphertext:
ciphertext_bytes = bytes.fromhex(
    "e8 e7 1b 9c 51 82 d5 07"
    "c6 d1 0f f0 6c 9b 72 07"
    "74 d3 f9 4f f2 32 d3 48"
    "44 f6 e5 94 cf 27 fa ee"
    "36 a8 d1 1d 9d ea cd b4"
    "1d 55 81 ea 1e 7d 1c e2"
    "3b fe fc d0 c9 96 3e aa"
    "e4 12 04 de ee 92 1c d5"
    "b8 c9 21 25 bd 71"
)       # Plaintext: It is perfectly acceptable to use ChaCha20 in real-world applications!

plaintext_bytes = chacha20_decryptor.update(ciphertext_bytes) + chacha20_decryptor.finalize()
print("Plaintext: " + str(plaintext_bytes, "utf-8"))