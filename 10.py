length = int(input())
array = list(map(int, input().split()))
result = []
maxLength=1
for i in array:
    if i == 1:
        n= array.count(1)
        if n > maxLength:
            maxLength = n
            result = 1
        continue
    current = i
    n=1
    while current**2 in array:
        current = current**2
        n+=1
    if n>maxLength:
        maxLength = n
        result = i
array = [result]
for i in range(maxLength-1):
   array.append(array[-1]**2)
print(maxLength)
print(" ".join(map(str, array)))


