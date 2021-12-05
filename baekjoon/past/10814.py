n = int(input())
data = []
for _ in range(n):
    x,y = input().split()
    data.append((int(x),y))

data.sort(key = lambda x:x[0])
for i,j in data:
    print(i,j)