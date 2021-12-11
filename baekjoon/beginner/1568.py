N = int(input())

toFar = 1
count = 0
while N>0:
    N -= toFar
    toFar+=1
    count+=1
    if toFar>N:
        toFar = 1
print(count)