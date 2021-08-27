N = int(input())
horror = list(map(int,input().split()))

horror.sort()
count = 0
group = 0
for x in horror:
    count+=1
    if x<=count:
        group += 1
        count=0

print(group)

