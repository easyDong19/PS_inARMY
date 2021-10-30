def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
edges = []
parent = [0] * n
all = 0 

for i in range(n):
    parent[i] = i

for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b)) 
    all += c

edges.sort()
cost = 0
for edge in edges:
    c,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        cost += c

print(all-cost)


    