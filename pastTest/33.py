n = int(input())
times = [], price = []
for i in range(n):
    t, p = map(int,input().split())  
    times.append(t)
    price.append(p)

dp = [-100]*(n+1)
maxvalue= 0

for i in range(n-1,-1,-1):
    atTime = i + times[i]
    if atTime <= n:
        dp[i] = max(maxvalue,dp[atTime]+price[i])
        maxvalue = dp[i]
    else:
        dp[i] = maxvalue
        



