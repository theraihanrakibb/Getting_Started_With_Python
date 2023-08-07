#         01234567890
parrot = "Blue is hot"
print(parrot)
print(parrot[-6])
print(parrot[-5])
print(parrot[11 - 6])
print(parrot[0:11])
print(parrot[:11])
print(parrot[0:])
print(parrot[:])
print(parrot[:5] + parrot[5:])
print(parrot[0:5:2])  # Bu
print(parrot[::-1])  # Reverse the string
print(parrot[::2])
number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
