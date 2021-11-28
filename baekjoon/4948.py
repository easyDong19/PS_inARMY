import math

result = []
rng = 246912 
lists = [True for _ in range(rng+1)]
lists[0]=False
lists[1]=False


for i in range(2, int(math.sqrt(rng))+1):
    if lists[i] == True:
        j = 2
        while i*j <= rng:
            lists[i*j] = False
            j +=1

while(1):
    n = int(input())
    if n==0: break
    count = 0

    for i in range(n+1,2*n+1):
        if lists[i] == True:
            count+=1
    
    print(count)
  

