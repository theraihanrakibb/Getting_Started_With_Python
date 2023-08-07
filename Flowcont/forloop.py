# parrot = "Norwegian Blue"
#
# for character in parrot:
#     print(character)

# number = "9,223;372:036 854,775;807"
number = input("Please eater a series of numbers, using any separators you like: ")
seperators = ""

for char in number:
    if not char.isnumeric():
        seperators = seperators + char

# print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print(sum([int(val) for val in values]))
