from itertools import combinations
n,m = map(int,input().split())
lists =list(map(int,input().split()))
summ = []
for i in combinations(lists,3):
    if sum(i)<=m:
        summ.append(sum(i))
print(max(summ))

