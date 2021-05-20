n = int(input())
boool = []
for i in range(n):
    r,e,c = map(int,input().split())
    check = 0
    if r+c<e: check = 1
    elif r+c>e: check = 2
    elif r+c==e: check = 3
    boool.append(check)

for i in boool:
    if i == 1:
        print("advertise")
    elif i == 2:
        print("do not advertise")
    elif i==3:
        print("does not matter")
    
    