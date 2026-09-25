#decode following into an ascii string:
n = 538357730889406264913494023630392172908367299690304928572219762649583643082782857709141783696377925090245220929432328346975546002711476829723085968286063806985723100502825777631323808504738627980523727052262803680456519717683124252325250956379346097568046

length = (n.bit_length() + 7) // 8
b = n.to_bytes(length, "big")           # integer -> bytes

print(b.decode())                       # bytes -> ASCII string (the answer)

# this is all claude code above as couldnt get the answer myself.

# this below is how it should be done, as taught by lecturer when i was stuck:

print("Lecturer method produces below: ")

# as n is one big number, cannot concatinate strings.
bignum = 538357730889406264913494023630392172908367299690304928572219762649583643082782857709141783696377925090245220929432328346975546002711476829723085968286063806985723100502825777631323808504738627980523727052262803680456519717683124252325250956379346097568046

#some algorithms only accept big numbers, such as RSA.
# have to try figure out how many bytes big is this number.
# Counting number of bits in bignum, converting num of bytes by dividing by 8, and rounding up. Hence +7 and // 8
size_in_bytes = (bignum.bit_length() + 7) // 8

x = bignum.to_bytes(size_in_bytes)

print(x)

# same thing with the b'' applies to lecturer method, this is a python thing. do a .decode("ascii") to remove this as before.
