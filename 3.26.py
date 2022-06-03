x = True
y = False
z = False
print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print(x or not y and not (x or not z))

x = False
y = True
z = False
print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print(x or not y and not (x or not z))

x = False
y = False
z = True
print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print(x or not y and not (x or not z))

x = False
y = True
z = True
print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print(x or not y and not (x or not z))

x = True
y = True
z = False
print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print(x or not y and not (x or not z))

