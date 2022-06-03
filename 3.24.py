x = True
y = False
z = False
print(not (y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

x = False
y = True
z = False
print(not (y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

x = False
y = False
z = True
print(not (y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

x = True
y = True
z = False
print(not (y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

x = True
y = False
z = True
print(not (y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)

x = False
y = True
z = True
print(not (y or not x and z) or z)
print(x and not (not y or z) or y)
print(not (x or y and z) or not x)