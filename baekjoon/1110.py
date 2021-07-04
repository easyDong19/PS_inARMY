N = int(input())
cycle = 0
new = N
while(True):
        new = new%10*10 + (new//10+new%10)%10
        cycle+=1

        if new==N:
            break
    
        
print(cycle)
