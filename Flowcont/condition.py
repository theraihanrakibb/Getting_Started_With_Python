age = int(input("How old are you? "))

if 16 <= age <= 65:  # if age >= 16 and age <= 65:
    # if age in range(16, 66):
    print("Have a good day at work")
else:
    print("You are too young to work")

print("-" * 40)

if age < 16 or age > 65:
    print("You are too young to work")
else:
    print("Have a good day at work")
