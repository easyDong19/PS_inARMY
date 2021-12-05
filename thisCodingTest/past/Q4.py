n = int(input())
coins = list(map(int,input().split()))

#코인을 오름차순으로 정렬
coins.sort()

target = 1
for coin in coins:
    if target>=coin:
        target+=coin
    else: break

print(target)