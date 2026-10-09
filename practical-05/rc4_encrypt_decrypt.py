from cryptography.hazmat.decrepit.ciphers.algorithms import ARC4
from cryptography.hazmat.primitives.ciphers import Cipher

# RC4 (ARC4) is a stream cipher, now considered broken due to biases in
# its keystream; prohibited in TLS since RFC 7465.

key = "thisisonelongkey"
key_bytes = bytes(key, "utf-8")
print("Key: " + key)

rc4_cipher = Cipher(ARC4(key_bytes), mode=None)
rc4_encryptor = rc4_cipher.encryptor()
rc4_decryptor = rc4_cipher.decryptor()

# Encrypting Code, commented out as per below:
#plaintext = "someplaintext"
#plaintext_bytes = bytes(plaintext, "utf-8")
#print("Plaintext: " + plaintext)

#ciphertext_bytes = rc4_encryptor.update(plaintext_bytes) + rc4_encryptor.finalize()
#ciphertext = ciphertext_bytes.hex()
#print("Ciphertext: " + ciphertext)

#plaintext_bytes_2 = rc4_decryptor.update(ciphertext_bytes) + rc4_decryptor.finalize()
#plaintext_2 = str(plaintext_bytes_2, "utf-8")
#print("Original Plaintext: " + plaintext_2)

# Decrypt code:


#Turn the hex from the sheet into bytes (fromhex ignores the spaces)
ciphertext_bytes = bytes.fromhex("eb 3e c6 68 de 7d 9e 02"
            "38 55 44 b9 69 1b c3 8b"
            "9d 56 ab 7d 9d 53 e8 02"
            "c1 86 85 1a d0 5e ad d0"
            "97 2a 75 56 e1 96 2a 60"
            "a1 f6 b2 86 bc 81 11 4a"
            "ac bd")

# The plaintext will read on output as "Plaintext: You should not use RC4 in real-world applications!"

# 3. Decrypt only
plaintext_bytes = rc4_decryptor.update(ciphertext_bytes) + rc4_decryptor.finalize()
print("Plaintext: " + str(plaintext_bytes, "utf-8"))