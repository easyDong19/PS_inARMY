x = int(input())

d = [0] * 30001                                                                                                                                                                                           #바텀업 문제임 (아래에서부터 위로)                             
for i in range(2, x+1):
    #현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] +1

    if i%2==0:
        #2로 나누고 된 값에 최솟값에 나눈 연산 +1을 더함
        d[i] = min(d[i],d[i//2]+1)
    if i%3==0:
        d[i] = min(d[i],d[i//3]+1)
    if i%5==0:
        d[i] = min(d[i],d[i//5]+1)

print(d[x])
        
