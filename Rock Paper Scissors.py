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


user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

random_number=random.randint(0,2)

print("You Chose : ")
if user_input==0:
    print(rock)
elif user_input==1:
    print(paper)
else:
    print(scissors)

computer=[rock,paper,scissors]
print("Computer Chose : \n")
print(computer[random_number])

if user_input==0 and random_number==2:
    print("You Win!!")
elif user_input==1 and random_number==0:
    print("You Win!!")
elif user_input==2 and random_number==1:
    print("You Win!!")
elif random_number==0 and user_input==2:
    print("You Lose!!")
elif random_number==1 and user_input==0:
    print("You Lose!!")
elif random_number==2 and user_input==1:
    print("You Lose!!")
else:
    print("Tie!!")
