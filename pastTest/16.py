n, m = map(int, input().split())
data = [] #초기 맵 리스트
temp =[[0] * m for _ in range(n)] #벽을 설치한 뒤에 맵 리스트

for _ in range(n):
    data.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

result = 0

#바이러스 퍼지게 하기
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx,ny)

#안전영역 크기계산
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score +=1

#울타리를 설치하면서 매번 안전 영역 크기계산
def dfs(count):
    global result
    #울타리가 3개인 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        #각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        result = max(result,get_score())
        #1. 리턴하게 되면
        return
    
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count+=1
                dfs(count)
                #2. 여기 코드가 시행됨
                data[i][j] = 0
                count-=1

dfs(0)