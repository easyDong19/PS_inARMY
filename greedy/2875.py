#n 여학생 m 남학생 k 인턴쉽참여
n,m,k = map(int,input().split())

team = 0
while(n>=2 and m>=1 and n+m-k>=3):
    n-=2
    m-=1
    team+=1

print(team)
