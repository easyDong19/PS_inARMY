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
parent = [0]*n

for i in range(n):
    parent[i] = i

for i in range(n):
    data = list(map(int,input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent,i,j)

plan = list(map(int,input().split()))

ret = "YES"
for i in range(m-1):
    if find_parent(parent,plan[i]-1) != find_parent(parent,plan[i+1]-1):
        ret = "NO"
        break
print(ret)

    
    