k = int(input())
lists = []
for _ in range(k):
    n,m = map(int, input().split())
    lists.append((n,m))

def fact(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*fact(num-1)


for list in lists:
    print(int(fact(list[1]) / (fact(list[0])*fact(list[1]-list[0]))))
