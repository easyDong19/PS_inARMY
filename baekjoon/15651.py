import itertools

n,m =map(int, input().split())
data = [i for i in range(1,n+1)]

for i in itertools.product(data,repeat = m):
    for j in i:
        print(j,end=" ")
    print()