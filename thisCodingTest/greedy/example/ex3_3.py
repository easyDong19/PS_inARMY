n,m = map(int,input().split())

maxx = -1
for _ in range(n):
    x = list(map(int,input().split()))
    maxx = max(maxx,min(x))

print(maxx)
    

    