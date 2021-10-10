n,m = map(int,input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)] #NxN 배열
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1

for i in range(1,n+1):
    #자기자신에게 가는 비용은 0
    graph[i][i] = 0

#플로이드 워셜 알고리즘
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

result = 0
for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        if graph[i][j]!=INF or graph[j][i]!=INF:
            count+=1
    if count==n:
        result+=1

print(result)