import random
import string

print("Password Generator")
print("------------------")

length = int(input("Enter password length: "))

print("\nChoose Password Type")
print("1. Letters Only")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols")

choice = int(input("Enter your choice (1-3): "))

match choice:
    case 1:
        characters = string.ascii_letters
    case 2:
        characters = string.ascii_letters + string.digits
    case 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    case _:
        print("Invalid choice!")
        exit()

password = "".join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:", password)