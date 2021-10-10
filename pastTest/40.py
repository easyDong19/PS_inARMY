import heapq

INF = int(1e9)
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

q = []
heapq.heappush(q,(0,1))
distance[1] = 0 #자기자신에게 가는 것은 0
while q:
    dist,now = heapq.heappop(q)
    if dist < distance[now]: continue
    for i in graph[now]:
        cost = i[1] + dist
        if cost<distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

rat = max(distance[1:])
print(distance.index(rat),rat,distance.count(rat))



    