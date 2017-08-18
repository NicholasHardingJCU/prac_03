def main():
    name = get_name()
    for char in name:
        if char.isalpha():
            print(name [::2])
    for char in name:
        if not char.isalpha():
            print("Invalid name..")
            name = get_name()
            print(name [::2])


def get_name():
    name = input("What is your name?")
    return name
main()