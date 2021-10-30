from collection import deque
import copy

v = int(input())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]
time = [0] * (v+1)

for i in range(1,v+1):
    data = list(map(int,input().split(0)))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def toplogy_sort():
    #리스트는 그냥 대입연산하면 값이 변경될 때 문제가 생길 수 있음
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i],result[now]+time[i])
            indegree[i] -=1
            if indegree[i] == 0:
                q.append(i)

                