n = int(input())
pos = list(map(int,input().split()))

pos.sort()
print(pos[(len(pos)-1)//2])