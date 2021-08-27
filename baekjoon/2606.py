from collections import deque
n = int(input())
edge = int(input())
graph = [[] for _ in range(n+1)]
infection = [-1]*(n+1)
for i in range(edge):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque([1])
infection[1] = 1
count = 0

while q:
    virus = q.popleft()
    for i in graph[virus]:
        if infection[i] == -1:
            count+=1
            q.append(i)
            infection[i] = 1

print(count)
    




