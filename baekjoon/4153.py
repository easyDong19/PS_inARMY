import sys
read = sys.stdin.readline

while 1:
    lists = list(map(int,read().split()))
    lists.sort()

    if lists[0]==0 and lists[1]==0 and lists[2]==0: break
    if lists[0]**2+lists[1]**2==lists[2]**2:
        print("right")
    else:
        print("wrong")