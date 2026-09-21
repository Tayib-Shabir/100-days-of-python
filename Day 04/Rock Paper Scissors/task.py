# Day4 project: Rock Paper Scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_moves = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:\n"))
if user_choice >= 0 and user_choice <= 2:
    print(f"You chose {game_moves[user_choice]}")

computer_choice = random.randint(0,2)
print(f"Computer chose:")
print(game_moves[computer_choice])

if user_choice >= 3 and user_choice < 0:
    print("You typed an invalid number!")
elif user_choice == computer_choice:
    print("Draw!")
elif user_choice == 0 and  computer_choice == 2:
    print("You win!")
elif user_choice == 0 and computer_choice == 1:
    print("You lose!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")

