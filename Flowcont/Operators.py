a = 12
b = 3

print(a + b)  # 15
print(a - b)  # 9
print(a * b)  # 36
print(a / b)  # 4.0
print(a // b)  # 4
print(a % b)  # 0 modulo

print()

for i in range(1, a // b):  # / not for int , // ---> int
    print(i)

print()

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)
print(((a + b) / 3 - 4) * 12)
