from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding  # to import padding as its in a different folder

# Padding Code:
padder = padding.PKCS7(algorithms.AES.block_size).padder()
unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()

# AES in ECB mode.  Each block is encrypted independently (no IV).
# Note: ECB is insecure for real use because identical plaintext blocks
# produce identical ciphertext blocks, revealing patterns in the data.

key = "thisisonelongkey"  # 16 bytes = AES-128
key_bytes = bytes(key, "utf-8")
print("Key: " + key)

# aes_cipher = Cipher(algorithms.AES(key_bytes), modes.ECB()) # For ECB mode

# For CBC mode
aes_cipher = Cipher(algorithms.AES(key_bytes),
                modes.CBC(bytearray(16)))

aes_encryptor = aes_cipher.encryptor()
aes_decryptor = aes_cipher.decryptor()

# Plaintext must be a multiple of the block size (16 bytes) in ECB mode
plaintext = "thebestplaintext"
plaintext_bytes = bytes(plaintext, "utf-8")
print("Plaintext: " + plaintext)

padded_bytes = padder.update(plaintext_bytes) + padder.finalize()   #for padded bytes
ciphertext_bytes = aes_encryptor.update(padded_bytes)
#ciphertext_bytes = aes_encryptor.update(plaintext_bytes) + aes_encryptor.finalize()
#ciphertext = ciphertext_bytes.hex()

# I want to decrypt a set cipher text:
ciphertext_bytes = bytes.fromhex(
    "39bd6a4bbb321733"
    "cada2340fbcbf8a5"
    "c9d8df6bde0a2596"
    "9d7b9813219aac0c"
    "4d4eb6520be87271"
    "d3198411d3a3ecc8")
print("Ciphertext: " + ciphertext_bytes.hex())

#print("Ciphertext: " + ciphertext)

padded_bytes_2 = aes_decryptor.update(ciphertext_bytes) # for padded only
plaintext_bytes_2 = unpadder.update(padded_bytes_2) + unpadder.finalize()   #again for padded

#plaintext_bytes_2 = aes_decryptor.update(ciphertext_bytes) + aes_decryptor.finalize()  # not needed for padded
plaintext_2 = str(plaintext_bytes_2, "utf-8")
print("Original Plaintext: " + plaintext_2)
