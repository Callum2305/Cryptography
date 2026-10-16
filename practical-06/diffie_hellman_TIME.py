import time
from cryptography.hazmat.primitives.asymmetric import dh

# Diffie-Hellman key exchange allows two parties to derive a shared
# secret over an insecure channel without prior shared keys.
# 512-bit is insecure; use 2048+ in practice.

# Depedning on the Key size, the time needed will be different:
# key_size = 512    Time recorded: 0.2587 seconds
# key_size = 1024   Time recorded: 2.6021 seconds
# key_size = 2048   Time recorded: 23.5370 seconds

# Most time is spent in the parameter generation (g, p)


# Change this to 512, 1024 or 2048 to compare running times.
KEY_SIZE = 2048

# Step 1: Alice and Bob agree on a set of parameters (g and p)

print("Generating " + str(KEY_SIZE) + "-bit parameters; this can take some time...")
start = time.perf_counter()
parameters = dh.generate_parameters(generator=2, key_size=KEY_SIZE)
param_time = time.perf_counter() - start
parameter_numbers = parameters.parameter_numbers()
print("g = " + str(parameter_numbers.g))
print("p = " + str(parameter_numbers.p))

# Step 2: Alice generates a public-private key pair and sends the
# public-key to Bob.

print()
print("Generating Alice's public-private key pair...")
start = time.perf_counter()
alice_private_key = parameters.generate_private_key()
alice_public_key = alice_private_key.public_key()
alice_keygen_time = time.perf_counter() - start

alice_private_key_private_numbers = alice_private_key.private_numbers()
print("a = " + str(alice_private_key_private_numbers.x))
alice_public_numbers = alice_public_key.public_numbers()
print("A = " + str(alice_public_numbers.y))

# Step 3: Bob generates a public-private key pair and sends the
# public-key to Alice.

print()
print("Generating Bob's public-private key pair...")
start = time.perf_counter()
bob_private_key = parameters.generate_private_key()
bob_public_key = bob_private_key.public_key()
bob_keygen_time = time.perf_counter() - start

bob_private_key_private_numbers = bob_private_key.private_numbers()
print("b = " + str(bob_private_key_private_numbers.x))
bob_public_numbers = bob_public_key.public_numbers()
print("B = " + str(bob_public_numbers.y))

# Step 4: Alice computes the shared key using information only she
# knows.

start = time.perf_counter()
alice_shared_key_bytes = alice_private_key.exchange(bob_public_key)
alice_exchange_time = time.perf_counter() - start
print()
print("Shared Key (according to Alice): " + alice_shared_key_bytes.hex())

# Step 5: Bob computes the shared key using information only he
# knows.

start = time.perf_counter()
bob_shared_key_bytes = bob_private_key.exchange(alice_public_key)
bob_exchange_time = time.perf_counter() - start
print()
print("Shared Key (according to Bob): " + bob_shared_key_bytes.hex())

# Timing summary

print()
print("--- Timing for " + str(KEY_SIZE) + "-bit key size ---")
print(f"Parameter generation (g, p):  {param_time:.4f} s")
print(f"Alice key pair generation:    {alice_keygen_time:.4f} s")
print(f"Bob key pair generation:      {bob_keygen_time:.4f} s")
print(f"Alice shared key computation: {alice_exchange_time:.4f} s")
print(f"Bob shared key computation:   {bob_exchange_time:.4f} s")
print(f"Total:                        {param_time + alice_keygen_time + bob_keygen_time + alice_exchange_time + bob_exchange_time:.4f} s")