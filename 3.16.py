x = True
y = False
print(not x and not y)
print(x or (not x and y))
print((not x and y) or y)

x = False
y = True
print(not x and not y)
print(x or (not x and y))
print((not x and y) or y)

x = True
y = True
print(not x and not y)
print(x or (not x and y))
print((not x and y) or y)

x = False
y= False
print(not x and not y)
print(x or (not x and y))
print((not x and y) or y)
