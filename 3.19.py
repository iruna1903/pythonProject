a = True
b = False
print(not (not a and not b) and a)
print(not (not a or not b) or a)
print(not (not a or not b) and b)

a = False
b = True
print(not (not a and not b) and a)
print(not (not a or not b) or a)
print(not (not a or not b) and b)

a = True
b = True
print(not (not a and not b) and a)
print(not (not a or not b) or a)
print(not (not a or not b) and b)

a = False
b = False
print(not (not a and not b) and a)
print(not (not a or not b) or a)
print(not (not a or not b) and b)