import os
import sys

# The One-Time Pad is provably secure if the key is truly random, as long as
# the message, and never reused.  Encryption and decryption are both XOR.


def generate_key(length):
    # os.urandom draws from the operating system's secure random number
    # generator, unlike the random module
    return os.urandom(length)


def encrypt_decrypt(input_, key):
    output = bytearray()
    # zip(..., strict=True) also catches a length mismatch, but the
    # check below reports it with a clearer message
    if len(input_) != len(key):
        raise ValueError("The input and key have different lengths!")
    for b, c in zip(input_, key, strict=True):
        output.append(b ^ c)
    return bytes(output)


if __name__ == "__main__":
    opts = ["-e", "-d"]
    if len(sys.argv) < 2 or sys.argv[1] not in opts:  # noqa: PLR2004
        print(sys.argv[0] + " [-e|-d]")
        sys.exit(0)

    if sys.argv[1] == opts[0]:
        plaintext_str = input("Plaintext: ")
        plaintext_bytes = bytes(plaintext_str, "utf-8")
        key_bytes = generate_key(len(plaintext_bytes))
        ciphertext_bytes = encrypt_decrypt(plaintext_bytes, key_bytes)
        print("Key (hex): " + key_bytes.hex())
        print("Ciphertext (hex): " + ciphertext_bytes.hex())
    elif sys.argv[1] == opts[1]:
        key_hex = input("Key (hex): ")
        key_bytes = bytes.fromhex(key_hex)
        ciphertext_hex = input("Ciphertext (hex): ")
        ciphertext_bytes = bytes.fromhex(ciphertext_hex)
        plaintext_bytes = encrypt_decrypt(ciphertext_bytes, key_bytes)
        plaintext_str = plaintext_bytes.decode("utf-8")
        print("Plaintext: " + plaintext_str)
