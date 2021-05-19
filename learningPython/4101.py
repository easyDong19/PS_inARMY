lists = []
while(1):
    a,b = map(int,input().split())
    if a!=0 and b!=0:
        lists.append((a,b))
    else: break

for list in lists:
    if list[0]-list[1]>0: print("Yes")
    else: print("No")
