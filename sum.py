n=int(input("Enter Number: "))
s=0
while n>0:
    i=n%10
    s=s+i
    n//=10
print(s)