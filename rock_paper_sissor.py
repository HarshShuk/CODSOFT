import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:

    user = input("\nEnter Rock, Paper or Scissors: ").lower()

    if user not in choices:
        print("Invalid Choice!")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):

        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("\nScore")
    print("You:", user_score)
    print("Computer:", computer_score)

    again = input("\nPlay Again? (yes/no): ").lower()

    if again != "yes":
        break

print("\nFinal Score")
print("You:", user_score)
print("Computer:", computer_score)
print("Thanks for Playing!")