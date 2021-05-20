n = int(input())
lists = []
for _ in range(n):
    a,b,c = map(int,input().split())
    prize = 0 
    if a==b==c: prize = 10000+a*1000
    elif a==b: prize = 1000+a*100
    elif b==c: prize = 1000+b*100
    elif c==a: prize = 1000+c*100
    else: prize =  max(a,b,c)*100
    lists.append(prize)    

print(max(lists))