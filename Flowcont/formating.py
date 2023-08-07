for i in range(1, 13):
    print("No. {0:2} square is {1:>3} and cubed is {2:>4}".format(i, i ** 2, i ** 3))  # Left

print()

for i in range(1, 13):
    print("No. {0:2} square is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))  # Left

print()

for i in range(1, 13):
    print("No. {0:2} square is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))  # Right

print()

for i in range(1, 13):
    print("No. {0:^2} square is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))  # Middle

print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))

print()

print(f"Pi is approximately {22 / 7:12.50f}")

pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
