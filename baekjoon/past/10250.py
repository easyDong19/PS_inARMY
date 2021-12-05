#테스트 케이스 
for _ in range(int(input())):
    h,w,n = map(int,input().split())
    #몫이 있는 경우와 딱 나눠 떨어지는 경우로 나눔
    #딱 나눠떨어지는 경우
    
    if n%h == 0:
        print(h*100+n//h)
    else:
        print(100*(n%h)+(n//h+1))
