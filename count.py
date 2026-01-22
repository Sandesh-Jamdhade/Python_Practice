#Digit Frequency
n=123
count=0
while n>0:
    i=n%10
    count+=1
    n=n//10
print(count)

#String Frequency
n="Sandesh"
count=0
for i in n:
    count+=1
print(count)