# Random Password Generator
#The objective of this project is to design and develop a random password generator
#application that allows users to generate strong and secure passwords with various criteria.
#The application should provide options for password length, character types, and special
#requirements.

#Golden Task

import random
import string
def get_random_password(length=10, uppercase=True, lowercase=True, digits=True, special_chars=True):
 all_chars = []
 if uppercase:
 all_chars += string.ascii_uppercase
 if lowercase:
 all_chars += string.ascii_lowercase
 if digits:
 all_chars += string.digits
 if special_chars:
 all_chars += string.punctuation
 password = ''.join(random.choice(all_chars) for _ in range(length))
 return password
if __name__ == "__main__":
 length = int(input("Enter the password length: "))
 uppercase = input("Include uppercase letters? (yes/no): ") == "yes"
 lowercase = input("Include lowercase letters? (yes/no): ") == "yes"
 digits = input("Include digits? (yes/no): ") == "yes"
 special_chars = input("Include special characters? (yes/no): ") == "yes"
 password = get_random_password(length, uppercase, lowercase, digits, special_chars)
 print(f"Generated password: {password}")