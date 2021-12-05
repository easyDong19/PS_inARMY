#손님에게 거슬러 줘야 할 돈이 N일 때 거슬러 줘야 할 동전의 최소 개수
coins = [500,100,50,10]
n = int(input())
        
count = 0
for coin in coins:       
    count += n // coin 
    n = n%coin
        
        
print(count)