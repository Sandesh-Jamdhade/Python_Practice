#Palindrome check for string
n="naman"
temp=n
rev=""
for i in n:
    rev=i+rev
if rev==temp:
    print("Palindrome")
else:
    print("Not Palindrome")