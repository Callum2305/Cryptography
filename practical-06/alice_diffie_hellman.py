from cryptography.hazmat.primitives.asymmetric import dh

# Alice's side of the Diffie-Hellman key exchange.
# Run this first, then run bob_diffie_hellman.py in a separate window.
# 512-bit is insecure; use 2048+ in practice.

# Step 1: Alice generates the public parameters (g and p) and sends
# them to Bob.

print("Generating parameters; this can take some time...")
parameters = dh.generate_parameters(generator=2, key_size=512)
parameter_numbers = parameters.parameter_numbers()
print("g = " + str(parameter_numbers.g))
print("p = " + str(parameter_numbers.p))

# Step 2: Alice generates a public-private key pair and sends the
# public key to Bob.

print()
print("Generating Alice's public-private key pair...")
alice_private_key = parameters.generate_private_key()
alice_private_key_private_numbers = alice_private_key.private_numbers()
print("a = " + str(alice_private_key_private_numbers.x))

alice_public_key = alice_private_key.public_key()
alice_public_numbers = alice_public_key.public_numbers()
print("A = " + str(alice_public_numbers.y))

print()
print("Send g, p and A to Bob.")

# Step 3 happens on Bob's machine. Alice receives Bob's public number B.

print()
B = int(input("Paste Bob's public number B: "))
bob_public_numbers = dh.DHPublicNumbers(B, parameter_numbers)
bob_public_key = bob_public_numbers.public_key()

# Step 4: Alice computes the shared key using information only she
# knows (a) and Bob's public number (B).

alice_shared_key_bytes = alice_private_key.exchange(bob_public_key)
print()
print("Shared Key (according to Alice): " + alice_shared_key_bytes.hex())
