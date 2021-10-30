def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,x)
    return parent[x]

def union_parent(a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int,input().split())
parent = [0] * (n+1)
#모든 간선들의 정보
edges = []

for i in range(n):
    parent[i] = i

for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b)) #a->b c의 비용이 듬

edges.sort()
last = 0
result = 0
for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(a,b)
        result += cost
        last = cost

print(result-last)



        