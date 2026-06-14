import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):

    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


print("\n===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

upper = input("Include uppercase letters? (y/n): ").lower() == "y"
digits = input("Include numbers? (y/n): ").lower() == "y"
symbols = input("Include special characters? (y/n): ").lower() == "y"

password = generate_password(length, upper, digits, symbols)

print("\nGenerated Password:")
print(password)