x = True
y = False
print(not (not x or y) or not x)
print(not (not x and not y) and x)
print(not (x or not y) or not y)

x = False
y = True
print(not (not x or y) or not x)
print(not (not x and not y) and x)
print(not (x or not y) or not y)

x = True
y = True
print(not (not x or y) or not x)
print(not (not x and not y) and x)
print(not (x or not y) or not y)

x = False
y = False
print(not (not x or y) or not x)
print(not (not x and not y) and x)
print(not (x or not y) or not y)