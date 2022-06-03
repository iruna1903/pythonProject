a = True
b = False
c = False
print(not (a or not b and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

a = False
b = True
c = False
print(not (a or not b and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

a = False
b = False
c = True
print(not (a or not b and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

a = True
b = True
c = False
print(not (a or not b and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

a = True
b = False
c = True
print(not (a or not b and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

a = False
b = True
c = True
print(not (a or not b and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)