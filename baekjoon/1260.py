from collections import deque

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited_D = [False] * (n+1)
vistied_B = [False] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

def dfs(graph,visited,v):
    visited[v] = True
    print(v,end= ' ')

    for node in graph[v]:
        if not visited[node]:
            dfs(graph,visited,node)

def bfs(graph,visited,v):
    visited[v] = True
    q = deque([v])
    while q:
        now = q.popleft()
        print(now,end= ' ')

        for node in graph[now]:
            if not visited[node]:
                visited[node] = True
                q.append(node)
    


dfs(graph,visited_D,v)
print()
bfs(graph,vistied_B,v)
