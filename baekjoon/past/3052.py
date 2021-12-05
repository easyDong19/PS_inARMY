numbers = []
for i in range(10):
    a = int(input())
    numbers.append(a)

numbers = [x%42 for x in numbers ]

numbers.sort()
count = 1
for i in range(0,9):
    if numbers[i] != numbers[i+1]: count+=1 

print(count)