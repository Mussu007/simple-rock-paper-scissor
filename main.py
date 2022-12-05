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

#Write your code below this line 👇

# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors

import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
else:
  print("Sorry you chose the wrong option")

comp_choice = random.randint(0, 2)
if comp_choice == 0:
  print(rock)
elif comp_choice == 1:
  print(paper)
elif comp_choice == 2:
  print(scissors)

if choice == comp_choice:
  print("Its a tie")
elif (choice == 0) and (comp_choice == 2):
  print("You win!")
elif (choice == 1) and (comp_choice == 0):
  print("You win!")
elif (choice == 2) and (comp_choice == 1):
  print("You win!")
else:
  print("You lose!")
