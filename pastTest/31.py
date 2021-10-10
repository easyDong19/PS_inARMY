for tc in range(int(input())):
    n,m = map(int,input().split())
    data = list(map(int,input().split()))
    
    dp = []
    index = 0
    for i in range(n):
        dp.append(data[index:index+m])
        index+=m

    for i in range(n):
        for j in range(1,m):
            if i == 0:
                left = 0
            else:
                left = dp[i-1][j-1]
            
            middle = dp[i][j-1]

            if i == n-1:
                right = 0
            else:
                right = dp[i+1][j-1]
            
            dp[i][j] = max(left,middle,right) + dp[i][j]
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)