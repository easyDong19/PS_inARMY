n = int(input())
lists = []
for _ in range(n):
    s = input()
    count = 0
    summ = 0
    for i in s:
        if i == 'O':
            count+=1
            summ +=count
        else:
            count=0
    lists.append(summ)

for i in lists:
    print(i)
