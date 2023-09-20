# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
password_option = int(
    input("Choose a generation option: 1 for simple, or 2 for complex.\n"))
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Simple Level - Order not randomized:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Complex Level - Order of characters randomized:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


def generate_simple_password(nr_letters, nr_symbols, nr_numbers):
    password = ""
    for char in range(1, nr_letters + 1):
        password += random.choice(letters)

    for char in range(1, nr_symbols+1):
        password += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
        password += random.choice(numbers)
    return password


def generate_complex_password():
    password_chars = []
    for char in range(1, nr_letters + 1):
        password_chars += random.choice(letters)

    for char in range(1, nr_symbols+1):
        password_chars += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
        password_chars += random.choice(numbers)

    complex_password = random.choice(password_chars)

    print(complex_password)


if password_option == 1:
    password = generate_simple_password(nr_letters, nr_symbols, nr_numbers)
    print(password)

if password_option == 2:
    generate_complex_password(nr_letters, nr_symbols, nr_numbers)
