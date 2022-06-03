a = True
b = False
print(not a and not b or a)
print(b or not a and not b)
print(b and not (a and not b))

a = False
b = True
print(not a and not b or a)
print(b or not a and not b)
print(b and not(a and not b))

a = True
b = True
print(not a and not b or a)
print(b or not a and not b)
print(b and not (a and not b))

a = False
b = False
print(not a and not b or a)
print(b or not a and not b)
print(b and not (a and not b))
