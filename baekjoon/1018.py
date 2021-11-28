n,m = map(int,input().split())
board = [[ "W" for _ in range(m)] for  _ in range(n)] 
origin = [[ "W" for _ in range(m)] for  _ in range(n)] 
for i in range(n):
    msg = input()
    for j in range(m):
        board[i][j] = msg[j]
        origin[i][j] = msg[j]


minn = 1e9
for pos_x in range(0,n-7):
    count = 0
    #보드 초기화
    for i in range(n):
        for j in range(m):
            board[i][j] = origin[i][j]

    for pos_y in range(0,m-7):
        for i in range(pos_x,pos_x+8):
            for j in range(pos_y,pos_y+8):
                #2번째 행부터 마지막 행까지 첫번째 열 보드가 위의 색과 같다면
                if i>pos_x and board[i-1][pos_y] == board[i][pos_y]:
                    if board[i][j] == 'W': board[i][j] = 'B'
                    else: board[i][j] = 'W'
                    count+=1
                #2번째 열부터 마지막 열까지 이전보드색과 현재색이 같다면
                elif j>pos_y and board[i][j-1] == board[i][j]:
                    if board[i][j] == 'W': board[i][j] = 'B'
                    else: board[i][j] = 'W'
                    count+=1
    minn = min(count,minn)

print(minn)
                