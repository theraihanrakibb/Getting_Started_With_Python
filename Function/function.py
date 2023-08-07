# def multiply():
#     result = 10.5 * 4
#     return result
#
#
# answer = multiply()
# print(answer)

def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    # backwards + string[::-1]
    # return backwards == string
    return string[::-2].casefold() == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    # return string[::-2].casefold() == string.casefold()
    return is_palindrome(string)


word = input("Please enter the word to check: ")

if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' isn't a palindrome".format(word))

answer = multiply(10.5, 5)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()

for value in range(1, 5):
    two_times = multiply(2, value)
    print(two_times)
