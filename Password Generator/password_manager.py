import random
import string 

def generate_password(min_length,numbers=True,special_characters=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    characters=letters 
    if numbers:
        characters += digits
    if special_characters: 
        characters +=special
    password=""
    fits_criteria= False 
    includes_number= False
    includes_special=False
    while not (fits_criteria and len(password)>= min_length):
        character=random.choice(characters)
        password += character 
        if character in digits:
            includes_number=True
        elif character in special:
            includes_special=True
        fits_criteria=True
        if numbers:
            fits_criteria=includes_number
        if special:
            fits_criteria=fits_criteria and includes_special 
    return password 
min_length=int(input("Enter the minimum password length:"))
includes_number=input("Do you want to have numbers in your password? answer yes or no ").lower()=="yes"
includes_special=input("Do you want to have special characters in your password? answer yes or no ").lower()=="yes"
pwd=generate_password(min_length,includes_number,includes_special)
print("your generated password is:",pwd)