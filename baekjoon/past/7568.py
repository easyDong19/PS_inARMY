n = int(input())
data = []
score = [1]*n #덩치등수 기록
for _ in range(n):
    x,y = map(int,input().split())
    data.append((x,y))

for i in range(0,n-1):
    for j in range(i+1,n):
        if data[i][0] > data[j][0] and data[i][1] > data[j][1]:
            score[j]+=1
        elif data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            score[i]+=1
        else: continue

for i in score:
    print(i, end=" ")