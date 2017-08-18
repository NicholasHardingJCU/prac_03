"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            calc_fahrenheit(celsius)
            print("Result: {:.2f} F".format(calc_fahrenheit(celsius)))
        elif choice == "F":
            fahrenheit = float(input("fahrenheit: "))
            calc_celsius(fahrenheit)
            print("Result: {:.2f} C".format(calc_celsius(fahrenheit)))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def calc_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def calc_celsius(fahrenheit):
    celsius = 5 / 9.0 * (fahrenheit - 32)
    return celsius

main()
