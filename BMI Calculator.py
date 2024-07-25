import math

print("BMI Calulator Version 2")

# Input From User
W = float(input("Enter Your Weight: "))
H = float(input("Enter Your Height: "))

# Checks if Inputs are correct
if H <= 0:
    print("Height is Invalid")

if W <= 0:
    print("Weight is Invalid")

# Calculation
B = W / (H*H)

# Displaying BMI Value
print("Your BMI is {:.2f}".format(B))

# Value to Result
if B < 18.5:
    print("You are Under weight")

elif 18.5 <= B <= 24.9:
    print("You are Normal Weight")

elif 25 <= B <= 29.9:
    print("You are Over weight")

elif B > 30:
    print("You are Obese")