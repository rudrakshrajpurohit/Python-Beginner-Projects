f = open("Names.txt" , "a")

while True:
    n = input("Enter Names of Students / Type <end> to end the program: ")
    if n.lower() == "end":
        break
    else:
        f.write(n + "\n")

f.close()
