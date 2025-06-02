import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"  #a random password with letters, digits, and special characters.
    
    # Start with an empty password
    password = ""
    
    # Add one random character at a time
    for i in range(length):
        random_character = random.choice(characters)
        password = password + random_character
    
    return password

# Generate and print a random 8-character password
password = generate_password(8)
print(f"Generated password: {password}")

