#Diamond Code
n = int(input("Enter number of rows (half): "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()

#Right Angled Triangle
n=int(input("Enter Number: "))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()

#Right Angled Triangle Inverted
n=int(input("Enter Number: "))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()