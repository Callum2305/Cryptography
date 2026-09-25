i = [65, 83, 67, 73, 73, 32, 115, 116, 97, 110, 100, 115, 32, 102,
111, 114, 32, 65, 109, 101, 114, 105, 99, 97, 110, 32, 83,
116, 97, 110, 100, 97, 114, 100, 32, 67, 111, 100, 101, 32,
102, 111, 114, 32, 73, 110, 102, 111, 114, 109, 97, 116, 105,
111, 110, 32, 73, 110, 116, 101, 114, 99, 104, 97, 110, 103,
101, 46]

## print([chr(c) for c in i])
# Better option below:
result = ""
for o in i:
    result += chr(o)

print(result)

#convert and arry of intergers into acsii characters using char() function, ord() function will do the opposite.