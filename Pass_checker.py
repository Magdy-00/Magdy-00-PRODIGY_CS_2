import string


def special_character(password):
    special_chars = string.punctuation
    for c in password:
        if c in special_chars:
            return True
    return False
while True:
    passw = input("Enter your password to be checked: ")

    # for length 
    if len(passw) < 8:
        print("Password must be at least 8 characters")

    #for digits and chars 
    if not any(char.isdigit() for char in passw) and any( char2.isalpha() for char2 in passw):
        print("Password must have both numbers and letters")

    #for upper chars
    if not any(char.isupper() for char in passw):
        print("Password must have at least one uppercase letter")

    #for lower cahrs
    if not any(char.islower() for char in passw):
        print("Password must have at least one lowercase letter")

    # For special chars
    if not special_character(passw):
        print("Password must have at least one special character")

    else:
        print("Password is valid")
        break
