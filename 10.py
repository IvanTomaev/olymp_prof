length = int(input())
array = list(map(int, input().split()))
ones = array.count(1)
result = []
result.append([1 for i in range(ones)])

numbers = (i for i in array if (int(i**0.5)**2 == i or (i**2) in array) and i != 1)

for i in numbers:
    current = i
    buffer = [current]
    while current ** 2 in array:
        while current in array:
            array.remove(current)
        current = current ** 2
        buffer.append(current)
    result.append(buffer)

result = sorted(result, key=lambda x:len(x), reverse=True)
print(len(result[0]))
for i in result[0]: print(i, end = " ")

