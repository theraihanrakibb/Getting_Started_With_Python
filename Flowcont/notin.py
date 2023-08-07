activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():  # .casefold() used upper and lowercase comparing
    print("But I want to go to the cinema")
