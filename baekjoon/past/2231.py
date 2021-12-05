n = int(input())
result = 0
for i in range(1,n):
    sum = i
    for x in str(i):
        sum += int(x)
    if sum == n:
        result = i
        break

print(result)

