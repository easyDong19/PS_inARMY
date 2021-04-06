54# n = 3^1 가운데 비어놓고 별이 찍힘
# n = 3^i 일때는 가운데 비어놓고 n=3^(i-1)일 때 별 배열이 찍힘 
def draw_star(n) :
    global Map
    
    if n == 3 :
        Map[0][:3] = Map[2][:3] = [1]*3
        Map[1][:3] = [1, 0, 1]
        return

    a = n//3
    draw_star(n//3)

    for i in range(3) :
        for j in range(3) :
            if i == 1 and j == 1 : 
                # 가운데는 비어놓는다
                continue
            for k in range(a) :
                Map[a*i+k][a*j : a*(j+1)] = Map[k][:a] # 핵심 아이디어

N = int(input())      

# 메인 데이터 선언
Map = [[0 for i in range(N)] for i in range(N)]

draw_star(N)

for i in Map :
    for j in i :
        if j :
            print('*', end = '')
        else :
            print(' ', end = '')
    print()