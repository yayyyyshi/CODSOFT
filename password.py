import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special=True):
    # Create a pool of characters to choose from
    character_pool = ''
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_digits:
        character_pool += string.digits
    if include_special:
        character_pool += string.punctuation

    # Ensure that the character pool is not empty
    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    # Generate a random password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 6): "))
            if length < 6:
                print("Password length should be at least 6 characters.")
                continue
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

        # Options for including character types
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        include_digits = input("Include digits? (y/n): ").lower() == 'y'
        include_special = input("Include special characters? (y/n): ").lower() == 'y'

        try:
            password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)
            print(f"Generated password: {password}")
        except ValueError as e:
            print(e)

        # Check if the user wants to generate another password
        next_generation = input("Do you want to generate another password? (yes/no): ")
        if next_generation.lower() != 'yes':
            break

    print("Thank you for using the Password Generator!")

if __name__ == "__main__":
    main()
