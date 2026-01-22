#Checks how many time the letter appears
n="sandesh jamdhade"
freq={}
for i in n:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

#check how many time the digit appears
n=11111222223333223839399993888
freq={}
while n>0:
    i=n%10
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
    n=n//10
print(freq)