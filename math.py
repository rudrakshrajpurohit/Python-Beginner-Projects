import random

# Defining Addition
def add():

    for i in range(11):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        ans = a + b
        
        while True:
            que = int(input(f"What is {a} + {b}?\n"))
            if que == ans:
                print("Answer is Correct")
                break
            else: 
                print("Incorrect Answer, TRY AGAIN")
                
    print("You Have Reached The END, Thank You For Completing")



# Defining Subtraction           
def sub():
    
    for i in range(11):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        ans = a -  b

        # Ensuring A is greater than B 
        if a > b: 
            while True:
                que = int(input(f"What is {a} - {b}?\n"))
                if que == ans:
                    print("Answer is Correct")
                    break
                else: 
                    print("Incorrect Answer, TRY AGAIN")
        else:
            continue

    print("You Have Reached The END, Thank You For Completing")

# Defining Multiplication      
def mul():

    for i in range(11):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        ans = a * b
        
        while True:
            que = int(input(f"What is {a} X {b}?\n"))
            if que == ans:
                print("Answer is Correct")
                break
            else: 
                print("Incorrect Answer, TRY AGAIN")
    
    print("You Have Reached The END, Thank You For Completing")

# Input Of Choice From user 
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exit")
    
    ch = int(input("Enter Your Choice: "))
    
    if ch == 1:
        add()
    elif ch == 2:
        sub()
    elif ch == 3:
        mul()
    elif ch == 4:
        break
    else:
        print("Invalid Choice")
