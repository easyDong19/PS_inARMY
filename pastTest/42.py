g = int(input())
p = int(input())

parent = [0] * (p+1)
plane = [[] for _ in range(p+1)]

for i in range(1,p+1):
    gi = int(input())
    for j in range(1,gi+1):
        #1~gi까지 
        plane[i].append(j)

print(plane)

