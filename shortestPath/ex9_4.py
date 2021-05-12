INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]


# 자기자신에게 가는거 초기화
for i in range(n+1):
    for j in range(n+1):
        if i==j:
            graph[i][j] = 0

#노드간 연결 정보 받기
for _ in range(m):
    a,b = map(int,input().split())
    # 양방향
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int,input().split())

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

distance = graph[1][k] + graph[k][x]

