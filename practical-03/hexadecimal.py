#Decode a string in hex into an ascii string.
# can also contactinate 2 strings to make it readlable:
#hex_str = ("string 1"
#           "string2")
# print(hex_string)


i = "456163682068657861646563696D616C20646967697420726570726573656E747320666F75722062697473206F722061206E6962626C652E"

# Shorthand way: print(bytes.fromhex(i))

# no direct hex to ascii conversiom, can go from bytes, hences the function above.
# this below solution is better for learning as it is step by step.

x = bytes.fromhex(i)

y = x.decode("ascii")

print(y)

# from bytes back to hex= 
z = x.hex()
print(z)