import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters = letters
    if numbers:
        characters += digits
    if special_characters: 
        characters += special
    password = ""
    fits_criteria = False 
    includes_number = False
    includes_special = False
    while not (fits_criteria and len(password) >= min_length):
        character = random.choice(characters)
        password += character 
        if character in digits:
            includes_number = True
        elif character in special:
            includes_special = True
        if not numbers or (numbers and includes_number):
            fits_criteria = True
        if not special_characters or (special_characters and includes_special):
            fits_criteria = True
    return password 

min_length = int(input("Enter the minimum password length: "))
includes_number = input("Do you want to have numbers in your password? Answer 'yes' or 'no': ").lower() == "yes"
includes_special = input("Do you want to have special characters in your password? Answer 'yes' or 'no': ").lower() == "yes"

pwd = generate_password(min_length, includes_number, includes_special)
print("Your generated password is:", pwd)