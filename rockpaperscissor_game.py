import random

'''
rock = 0
paper = 1
scissor = 2
'''

# Dictionaries
dict = {0 : "Rock", 1 : "Paper", 2 : "Scissor"}
rev_dict = {"rock": 0,"paper" : 1, "scissor" : 2}

# Inputs of User and Computer
comp = random.choice([0 , 1, 2])
user_choice = input("Enter Your choice: ")
user = rev_dict[user_choice]

# Computing and printing the result
print(f"You Chose: {user_choice} \n The Computer Chose: {dict[comp]}")

if comp == user:
    print("Draw")
else:
    if comp == 0 and user == 1:
        print("You Win")

    elif comp == 0 and user == 2:
        print("You Lose")

    elif comp == 1 and user == 0:
        print("You Lose") 

    elif comp == 1 and user == 2:
        print("You Win")

    elif comp == 2 and user == 0:
        print("You Win")

    elif comp == 2 and user == 1:
        print("You Lose") 
    else: 
        print("Something is wrong")
 