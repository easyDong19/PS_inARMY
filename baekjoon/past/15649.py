import itertools

n,m = map(int,input().split())
data = [i for i in range(1,n+1)]

for i in (itertools.permutations(data,m)):
    for x in i:
        print(x,end=" ")
    print()

