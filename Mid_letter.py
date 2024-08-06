s = input("Enter a Word: ")

a = int(len(s))

def mid(a):
    if a%2 == 0:
        print("")
    else:
        mid = a//2
        print(s[mid])

mid(a)