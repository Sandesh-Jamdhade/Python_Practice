l1=[8,8,1,2,6,1,3,2,9,1,2]
n=len(l1)
s=[]
for i in range(n):
    if l1[i] not in s:
        s.append(l1[i])
print(s)

