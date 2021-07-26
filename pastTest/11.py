#보드의 크기 N
#사과의 개수 K
N = int(input())
K = int(input()) 

#NxN 크기의 보드
board = [[0 for _ in range(N)] for __ in range(N)]


for _ in range(K):
    x,y = map(int,input().split())
    #사과는 1
    board[x][y] = 1

#뱀의 방향 변환 횟수 L
L = int(input())

times = [0 for _ in range(L)]
for _ in range(L):
    # X:초 C: 방향 L OR D 90 degree turn 
    X,C = input().split()
    times.append((X,C))


#동서남북
dx = [1,-1,0,0]
dy = [0,1,-1,1]

#걸린시간
result = 0

#뱀이 있는 경우 2
board[0][0] = 2
#뱀 현재 머리 위치
x = 0; y= 0
direct = 0

#시뮬레이션
while True:
    result +=1
    if times[dircet][0] == result:
        
    #방향으로 이동
    head_x = x + dx[direct]; head_y = y + dy[direct]
    if head_x<0 or head_x>N or head_y<0 or head_y>N: break








