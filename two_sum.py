a=[2,3,4,7]
n=len(a)
target=9
for i in range(n):
    for j in range(i+1,n):
        if a[i]+a[j]==target:
            print([i,j])