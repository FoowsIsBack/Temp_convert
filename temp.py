#Dave.py
import os

def clear():
    if os.name == 'nt':  
        os.system('cls')
    else:
        os.system('clear')

print("-------------------------")
print("  Temperature Converter")
print("-------------------------")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Exit")
print("-------------------------")
choice = int(input("Choice: "))
clear()

if choice == 1:
    print("-------------------------")
    print("  Celsius to Fahrenheit")
    print("-------------------------")
    celsius = float(input("Enter the Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    clear()
    print("-------------------------")
    print("  Celsius to Fahrenheit")
    print("-------------------------")
    print(f"Fahrenheit is: {fahrenheit:.1f}")
    print("-------------------------")

if choice == 2:
    print("-------------------------")
    print("  Fahrenheit to Celsius")
    print("-------------------------")
    fahrenheit = float(input("Enter the Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    clear()
    print("-------------------------")
    print("  Fahrenheit to Celsius")
    print("-------------------------")
    print(f"Celius is: {celsius:.5f}")
    print("-------------------------")
 
if choice == 3:
    print("-------------------------")
    print(" Thank you & Good bye! ")
    print("-------------------------")
#Dave.py