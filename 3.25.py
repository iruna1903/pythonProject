a = True
b = False
c = False
print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and b or not (a or not c))

a = False
b = True
c = False
print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and b or not (a or not c))

a = False
b = False
c = True
print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and b or not (a or not c))

a = True
b = True
c = False
print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and b or not (a or not c))

a = True
b = False
c = True
print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and b or not (a or not c))

a = False
b = False
c = True
print(not (a and b) and (not a or not c))
print(not (a and not b) or (a or not c))
print(a and b or not (a or not c))