import math

n = int(input())
lists = list(map(int,input().split()))

prime = 0
isprime = True
for i in lists:
    #1은 소수가 아님
    if i == 1:
        continue

    #범위를 잘생각해야함
    for j in range(2,int(math.sqrt(i)+1)):
        if i % j == 0:
            isprime = False
            break

    if isprime == True:
        prime+=1
    else:
        isprime = True

print(prime)            
    
        

