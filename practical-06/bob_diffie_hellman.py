from cryptography.hazmat.primitives.asymmetric import dh

# Bob's side of the Diffie-Hellman key exchange.
# Run alice_diffie_hellman.py first and copy g, p and A from it.

# Step 1: Bob receives the public parameters (g and p) from Alice and
# rebuilds them from the integers.

g = int(input("Paste g: "))
p = int(input("Paste p: "))
parameter_numbers = dh.DHParameterNumbers(p, g)
parameters = parameter_numbers.parameters()

# Step 2 happens on Alice's machine. Bob receives Alice's public
# number A.

A = int(input("Paste Alice's public number A: "))
alice_public_numbers = dh.DHPublicNumbers(A, parameter_numbers)
alice_public_key = alice_public_numbers.public_key()

# Step 3: Bob generates a public-private key pair and sends the
# public key to Alice.

print()
print("Generating Bob's public-private key pair...")
bob_private_key = parameters.generate_private_key()
bob_private_key_private_numbers = bob_private_key.private_numbers()
print("b = " + str(bob_private_key_private_numbers.x))

bob_public_key = bob_private_key.public_key()
bob_public_numbers = bob_public_key.public_numbers()
print("B = " + str(bob_public_numbers.y))

print()
print("Send B to Alice.")

# Step 5: Bob computes the shared key using information only he
# knows (b) and Alice's public number (A).

bob_shared_key_bytes = bob_private_key.exchange(alice_public_key)
print()
print("Shared Key (according to Bob): " + bob_shared_key_bytes.hex())
