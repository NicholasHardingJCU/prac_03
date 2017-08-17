name = input("What is your name? ")
for char in name:
    if not char.isalpha():
        print("Invalid name..")
        name = input("What is your name? ")