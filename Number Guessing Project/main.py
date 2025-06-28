import random
import art

print(art.logo)
print("Welcome to a Number Guessing Game!")
print("I am thinking of a number between 1 to 100")

random_number = random.randint(1,100)

difficulty = input("Choose a difficulty . Type 'easy' or 'hard' : ").lower()
user="win"
print(random_number)

def game(attempts):
    while attempts>0:
        print(f"You have {attempts} remaining to guess the number.")
        user_input = int(input("Make a guess : "))
        if user_input > random_number:
            print("Too High.")
            print("Guess Again.")
            attempts-=1
        elif user_input < random_number:
            print("Too Low.")
            print("Guess Again.")
            attempts-=1
        elif user_input == random_number:
            print(f"You got it. The answer was {user_input}!")
            break
        if attempts==0:
            print("You Lose , Out of attempts . Try Again !")


if difficulty == "easy":
    game(10)
elif difficulty =="hard":
    game(5)





