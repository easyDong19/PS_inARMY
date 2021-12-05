import math

m = int(input())
n = int(input())
array = [True for i in range(n+1)] #1~n까지 소수 
array[1] = False
lists = [] #정답을 담을 리스트

for i in range(2,int(math.sqrt(n))+1):
    if array[i] == True:
        j = 2
        while i*j <= n:
            array[i*j] = False
            j+=1

for i in range(m,n+1):
    if array[i] == True:
        lists.append(i)

        
if len(lists) != 0:
    print(sum(lists))
    print(lists[0])
else:
    print(-1)
