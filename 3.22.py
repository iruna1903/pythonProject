x = True
y = False
z = False
print(not (x or not y and z))
print(y or (x and not y or z))
print(not (not x and y or z))

x = False
y = True
z = False
print(not (x or not y and z))
print(y or (x and not y or z))
print(not (not x and y or z))

x = False
y = False
z = True
print(not (x or not y and z))
print(y or (x and not y or z))
print(not (not x and y or z))

x = True
y = True
z = False
print(not (x or not y and z))
print(y or (x and not y or z))
print(not (not x and y or z))

x = True
y = False
z = True
print(not (x or not y and z))
print(y or (x and not y or z))
print(not (not x and y or z))

x = False
y = True
z = True
print(not (x or not y and z))
print(y or (x and not y or z))
print(not (not x and y or z))