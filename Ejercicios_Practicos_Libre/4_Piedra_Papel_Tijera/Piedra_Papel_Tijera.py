import random

# ASCII art

Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# Lifes

Player_Lifes = 3
Computer_Lifes = 3

# Introduction

print("Welcome to Rock, Paper & Scissors game!")
print("Made by Gonzalo Martos Conesa")

# Loop

while Player_Lifes >= 1 and Computer_Lifes >= 1:
    try:

        # Player's choice

        Player = int(input('Type "1" for Rock, "2" for Paper, "3" for Scissors\n'))

        if Player == 1:
            print(f"You choose {Rock}")
        elif Player == 2:
            print(f"You choose {Paper}")
        elif Player == 3:
            print(f"You choose {Scissors}")
        else:
            print("Please choose a valid number")
            continue

        # Computer's choice

        Computer = random.randint(1,3)

        if Computer == 1:
            print(f"Computer choose {Rock}")
        elif Computer == 2:
            print(f"Computer choose {Paper}")
        else:
            print(f"Computer choose {Scissors}")

        # Fight

        if Player == Computer:
            print("Draw!")
            continue
        elif Player - Computer == 1:
            print("You Win!")
            Computer_Lifes -=1
            continue
        elif Player - Computer == -2:
            print("You Win!")
            Computer_Lifes -= 1
            continue
        else:
            print("You Lose!")
            Player_Lifes -= 1
            continue
    
    except ValueError:
        print("Please, choose a valid number")
        continue

# Ending

if Player_Lifes < 1:
    print("You lose all lifes")
    print("Game Over!")
else:
    print("The Computer lose all lifes")
    print("Congratulations! You are the Winner!")