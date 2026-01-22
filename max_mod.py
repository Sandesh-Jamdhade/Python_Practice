l1=[10,23,43,12,20,11]
l2=[3,2,4,2,7,3]
l3=[]
i=0
while i<len(l1):
    l3.append(l1[i]%l2[i])
    i+=1
print(l3)
print(max(l3))
