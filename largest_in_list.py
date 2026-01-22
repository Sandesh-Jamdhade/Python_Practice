lst=[10,2,12,23,32,45]
largest=lst[0]
for i in lst:
    if i > largest:
        largest = i
print(largest)