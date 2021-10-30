def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = x
    return parent[x]

#합치기 연산
def union(a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

#같은 팀 여부 확인
def check_team(a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a==b:
        return "YES"
    else:
        return "NO"


n,m = map(int,input().split())
parent = [0] * (n+1)

#자기 자신을 부모로 초기화
for i in range(0,n+1):
    parent[i] = i


#팀 합치기 0 a b
#같은 팀 여부 확인 1 a b
result = []
for _ in range(m):
    oper,a,b = map(int,input().split())
    if oper == 0:
        union(a,b)
    elif oper == 1:
        result.append(check_team(a,b))

for word in result:
    print(word)
