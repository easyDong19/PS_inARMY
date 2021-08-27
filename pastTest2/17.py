from collections import deque

n, k = map(int,input().split())
board = [] # n *n 시험관
virus = [] # 바이러스의 좌표를 담을 리스트
for i in range(n):
    board.append(list(map(int,input().split())))
    for j in range(n):
        if board[i][j] != 0:
            virus.append((board[i][j],i,j,0)) #바이러스 정보, 좌표, 초를 집어 넣는다

virus.sort() #바이러스 순으로 오름차순
q = deque(virus)

target_s,target_x,target_y = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

    #q가 빌 동안
while q:
     now = q.popleft()
     vi = now[0], x = now[1], y = now[2], second = now[3]

     if second == target_s:
         break
    #4가지 방향으로 탐색
     for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<n and nx>=0 and ny<n and ny>=0:
            if board[nx][ny] == 0:
                board[nx][ny] = vi
                q.append((board[nx][ny],nx,ny,second+1))

print(board[target_x-1][target_y-1])