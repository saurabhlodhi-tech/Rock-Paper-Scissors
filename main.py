import random

choices = ["rock", "paper", "scissors"]
while True:
 user_choice = input("Enter your choice :").lower()

 if user_choice not in choices:
    print("Invalid choice! Please choose rock, paper or scissors.")
    continue

 computer_choice = random.choice(choices)

 if user_choice == computer_choice:
    print("Draw!")
 elif user_choice == "scissors" and computer_choice == "paper":
    print("You Win")
 elif user_choice =="rock" and computer_choice == "scissors":
    print("You Win")
 elif user_choice =="paper" and computer_choice == "rock":
    print("You Win")
 else:
    print("Computer wins !")

 play_again = input("play again? (yes/no): ").lower()

 if play_again =="no":
   break

    




