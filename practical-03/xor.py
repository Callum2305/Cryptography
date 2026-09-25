#lecturer method....
# demonstrate the following:

#commutativity:
# A XOR B = B XOR A

A_hex_string = "67af3f01"
B_hex_string = "9fa76fbb"
C_hex_string = "80bc1b21"
Z_hex_string = "00000000"

A_bytes = bytes.fromhex(A_hex_string)
B_bytes = bytes.fromhex(B_hex_string)
C_bytes = bytes.fromhex(C_hex_string)
Z_bytes = bytes.fromhex(Z_hex_string)


# ^ built in python bitwise XOR function. Doesnt do sequence of bytes, so we need a method of XORing long sequence of bytes

def  xor_bytes(bytes_seq_1, bytes_seq_2):
    """preforms a XOR on two byte sequences"""
    return bytes([a ^ b for a, b in zip(bytes_seq_1, bytes_seq_2)])

t0 = xor_bytes(A_bytes, B_bytes)
t1 = xor_bytes(B_bytes, A_bytes)

print(t0.hex())
print(t1.hex())

# Associative:
# Doesnt matter where you put the brackets. Associating them differently.
t2 = xor_bytes(A_bytes, xor_bytes(B_bytes, C_bytes))
t3 = xor_bytes(xor_bytes(A_bytes, B_bytes), C_bytes)

print(t2.hex())
print(t3.hex())

# Identity: xor value by 0 gives the same value
t4 = xor_bytes(A_bytes, Z_bytes)
print(t4.hex())
print(A_hex_string)

# XOR  a value by itself, it will be all zeros
t5 = xor_bytes(B_bytes, B_bytes)
print(t5.hex())
print(Z_hex_string)