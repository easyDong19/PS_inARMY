
N = int(input())
lists = list(map(int,input().split(" ")))

lists.sort()

target = 1
for x in lists:
    if target < x:
        break
    target += x