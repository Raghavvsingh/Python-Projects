import art

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

print(art.logo)

repeat=True
first_number=float(input("What's the first number?: "))

def calculation(f_number):
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    s_number=float(input("What's the next number?: "))
    if operation=="+":
        ans=add(f_number,s_number)
        print(f"{f_number}+{s_number} = {ans}")
        return ans
    elif operation=="-":
        ans=subtract(f_number,s_number)
        print(f"{f_number}-{s_number} = {ans}")
        return ans
    elif operation=="*":
        ans=multiply(f_number,s_number)
        print(f"{f_number}*{s_number} = {ans}")
        return ans
    elif operation=="/":
        ans=divide(f_number,s_number)
        print(f"{f_number}/{s_number} = {ans}")
        return ans
    else:
        print("Wrong Input.")
        return "None"

answer=calculation(first_number)
while repeat==True:
    user_input =input(f"Type 'y' to continue calculating with {answer} , or type 'n' to start a new calculation.")
    if user_input=="y":
        answer=calculation(answer)
    else:
        first_number = int(input("What's the first number?: "))
        answer=calculation(first_number)




