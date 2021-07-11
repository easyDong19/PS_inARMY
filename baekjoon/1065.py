x = int(input())
count = 0
for i in range(1,x+1):
    if i < 100:
        count+=1
    else:
        x = str(i)
        if int(x[0])+int(x[2])==int(x[1])*2:
            count+=1

print(count)