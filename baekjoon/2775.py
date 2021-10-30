T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    
    lists = [i for i in range(1,n+1)]
    #1~n
    for _ in range(k):
        for i in range(1,n):
            lists[i] = lists[i-1] + lists[i]
    
    print(lists[-1])