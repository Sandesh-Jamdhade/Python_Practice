#Sorting without inbuilt methods
a=[1,10,2,30,34,5,32,2,1]
n=len(a)
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)