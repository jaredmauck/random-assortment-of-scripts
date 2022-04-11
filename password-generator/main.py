#Password Generator Project
import random
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_total_letters= int(input("How many characters would you like in your password?\n"))
nr_uppercase_letters= int(input("How many uppercase letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

nr_lowercase_letters = nr_total_letters - nr_uppercase_letters - nr_numbers - nr_symbols

a = random.choices(lowercase_letters, k=nr_lowercase_letters)
b = random.choices(uppercase_letters, k=nr_uppercase_letters)
c = random.choices(numbers, k=nr_numbers)
d = random.choices(symbols, k=nr_symbols)

z = a + b + c + d

random.shuffle(z)
total = ""
for passw in z:
    total += passw
print(f"Here is your password: {total}")
