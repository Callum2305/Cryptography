from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def check(name, mode, key_hex, plaintext_hex, expected_hex):
    aes_cipher = Cipher(algorithms.AES(bytes.fromhex(key_hex)), mode)
    aes_encryptor = aes_cipher.encryptor()
    ciphertext_bytes = aes_encryptor.update(bytes.fromhex(plaintext_hex)) + aes_encryptor.finalize()
    ciphertext = ciphertext_bytes.hex()
    print(name)
    print("  Got:      " + ciphertext)
    print("  Expected: " + expected_hex)
    print("  " + ("PASS" if ciphertext == expected_hex else "FAIL"))

iv = bytes.fromhex("00000000000000000000000000000000")
zero_block = "00000000000000000000000000000000"

check("ECBGFSbox128", modes.ECB(),
      "00000000000000000000000000000000",
      "f34481ec3cc627bacd5dc3fb08f273e6",
      "0336763e966d92595a567cc9ce537f5e")

check("CBCKeySbox192", modes.CBC(iv),
      "e9f065d7c13573587f7875357dfbb16c53489f6a4bd0f7cd",
      zero_block,
      "0956259c9cd5cfd0181cca53380cde06")

check("CFB128VarKey256", modes.CFB(iv),
      "8000000000000000000000000000000000000000000000000000000000000000",
      zero_block,
      "e35a6dcb19b201a01ebcfa8aa22b5759")

check("OFBVarKey256", modes.OFB(iv),
      "8000000000000000000000000000000000000000000000000000000000000000",
      zero_block,
      "e35a6dcb19b201a01ebcfa8aa22b5759")