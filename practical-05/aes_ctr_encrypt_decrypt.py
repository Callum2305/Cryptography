import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# AES in CTR mode turns a block cipher into a stream cipher by
# encrypting successive counter values and XORing with plaintext.
# No padding needed since it operates as a stream cipher.

# Fresh key for this standalone run; never overlap counter ranges under a key.
key_bytes = os.urandom(32)
# 96-bit message nonce followed by a 32-bit initial counter, big-endian.
# Limit messages to fewer than 2**32 blocks and do not reuse message nonces.
nonce_bytes = os.urandom(12) + bytes(4)

aes_ctr_cipher = Cipher(algorithms.AES(key_bytes), mode=modes.CTR(nonce_bytes))
aes_ctr_encryptor = aes_ctr_cipher.encryptor()
aes_ctr_decryptor = aes_ctr_cipher.decryptor()

plaintext = "someplaintext"
plaintext_bytes = bytes(plaintext, "utf-8")
print("Plaintext: " + plaintext)

ciphertext_bytes = aes_ctr_encryptor.update(plaintext_bytes) + aes_ctr_encryptor.finalize()
ciphertext = ciphertext_bytes.hex()
print("Ciphertext: " + ciphertext)

plaintext_bytes_2 = aes_ctr_decryptor.update(ciphertext_bytes) + aes_ctr_decryptor.finalize()
plaintext_2 = str(plaintext_bytes_2, "utf-8")
print("Original Plaintext: " + plaintext_2)
