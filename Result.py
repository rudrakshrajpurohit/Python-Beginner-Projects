# Input from user
M = float(input("Enter Marks of Mathematics: "))
H = float(input("Enter Marks of Hindi: "))
S = float(input("Enter Marks of Science: "))

# Calculating Total Aggregate
R = ((M + S + H)/300) * 100

# printing Total Aggregate
if R < 40:
    print(''' Your aggregate is: {:.2f}%
          Minimum Pass Aggregate is 40%
          NOT PROMOTED to next class'''.format(R))
else: 
    print(''' Your aggregate is : {:.2f}%
          PROMOTED TO NEXT CLASS'''.format(R))
    
# Evaluating Individual Subject Aggregate
if M < 33:
    print(''' You scored {} in Mathematics
          Minimum Pass Score is 33
          FAILED IN MATHEMATICS'''.format(M))
else:
    pass
if H < 33:
    print(''' You scored {} in Mathematics
          Minimum Pass Score is 33
          FAILED IN MATHEMATICS'''.format(H))
else:
    pass
if S < 33:
    print(''' You scored {} in Mathematics
          Minimum Pass Score is 33
          FAILED IN MATHEMATICS'''.format(S))
else:
    pass

# Printing Grade of Student
if 90 <= R <= 100:
    print("Your Grade is: A+")
elif 80 <= R < 90:
    print("Your Grade is: A")
elif 70 <= R < 80:
    print("Your Grade is: B+")
elif 60 <= R < 70:
    print("Your Grade is: B")
elif 50 <= R < 60:
    print("Your Grade is: C")
elif 40 <= R < 50:
    print("Your Grade is: D")
else:
    print("Your Grade is: F")
