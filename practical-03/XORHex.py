h1 = input("Enter first hex string: ")
h2 = input("Enter second hex string: ")

a = bytes.fromhex(h1)
b = bytes.fromhex(h2)

result = []
for i in range(len(a)):
    result.append(a[i] ^ b[i])   # XOR byte i of each string

print(bytes(result).hex())

#Inputs:    1c0111001f010100061a024b53535009181c
#           686974207468652062756c6c277320657965

#Output: 746865206b696420646f6e277420706c6179
