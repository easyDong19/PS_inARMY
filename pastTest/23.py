N = int(input())
lists = []
for _ in range(N):
    lists.append(input().split())

lists.sort(key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in lists:
    print(i[0])