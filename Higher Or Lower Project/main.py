import random
import art
import game_data


def random_number():
    random_number=random.randint(0,len(game_data.data)-1)
    return random_number

random_data1 = random.randint(0,len(game_data.data)-1)
random_data2 = random.randint(0,len(game_data.data)-1)

def display(rdata1 , rdata2):
    print("\n"*100)
    print(art.logo)
    print(f"Compare A: {game_data.data[rdata1]["name"]} , a {game_data.data[rdata1]["description"]} , from {game_data.data[rdata1]["country"]}")
    print(art.vs)
    print(f"Compare B: {game_data.data[rdata2]["name"]} , a {game_data.data[rdata2]["description"]} , from {game_data.data[rdata2]["country"]}")

def check_result(rdata1,rdata2):
    if game_data.data[rdata1]["follower_count"] > game_data.data[rdata2]["follower_count"]:
        ans = "A"

    elif game_data.data[rdata1]["follower_count"] < game_data.data[rdata2]["follower_count"]:
        ans = "B"

    return ans

result = True
count=0
display(random_data1,random_data2)

while result!=False:
    user_input=input("Who has more followers ? A or B: ")
    answer=check_result(random_data1,random_data2)
    if user_input=="A" and answer=="A":
        count+=1
        print(f"You are right! Current Score: {count} ")
        r=random_number()
        display(random_data1,r)
    else:
        print(f"Sorry that's Wrong! Final Score: {count}")
        result=False
