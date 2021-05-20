#과자 가격, 개수, 자금
k,n,m = map(int,input().split())

if k*n-m>0: print(k*n-m)
else: print(0)

