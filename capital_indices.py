s = input("Enter a word: ")
l = []

for i in range(len(s)):
    if s[i].isupper():
        l.append(i)

print(l)
