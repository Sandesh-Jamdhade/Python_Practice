#Checking Palindrome
n=121
temp=n
palindrome=0
while n>0:
    i=n%10
    palindrome=palindrome*10+i
    n=n//10
if temp==palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")