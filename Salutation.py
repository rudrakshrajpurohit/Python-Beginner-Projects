import datetime

#Input From User
N = input("Enter Your Name: \n")

# Processing & Printing
D = datetime.datetime.now()

Letter = '''Good Afternoon {},
            You are Selected!  
            {}'''.format(N, D.strftime("%x"))
  
print(Letter)
