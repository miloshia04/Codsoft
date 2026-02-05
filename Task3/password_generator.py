import random
import string

def generate_password():
    print(" Password Generator ")
    try:
        length = int(input("how long do you want passwod to be: "))
        if length < 4:
            print("Note:use atleast 8 or more characters")
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))
        print(f"\nYour generated password is: {password}")
        print("-" * 26)
    except ValueError:
        print("Invalid input. Please enter a number.")
if __name__ == "__main__":
    generate_password()
