import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

l=""
for i in range(1,nr_letters+1):
    random_letters = random.randint(0, nr_letters)
    l+=letters[random_letters]

s=""
for i in range(1,nr_symbols+1):
    random_symbols= random.randint(0,nr_symbols)
    s+=symbols[random_symbols]

n=""
for i in range(1,nr_numbers+1):
    random_numbers=random.randint(0,nr_numbers)
    n+=numbers[random_numbers]

# print(l+s+n)
#Easy version complete
easy_password=l+s+n
total_characters = nr_letters + nr_numbers + nr_symbols
final_password=""
for i in range(1,total_characters+1):
    random_number = random.randint(0,total_characters-1)
    final_password+=easy_password[random_number]

print(final_password)

#Hard version Complete