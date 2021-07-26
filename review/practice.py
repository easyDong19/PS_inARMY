from collections import deque

def DFS(graph, start, visited):
    #방문 처리
    visited[start] = True
    print(graph[start])
    
    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, visited)

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(graph[i])
                visited[i] = True
            
            
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9