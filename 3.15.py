a = True
b = False
print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)

a = True
b = True
print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)

a = False
b = False
print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)

a = False
b = True
print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)


