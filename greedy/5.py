n,m = map(int,input().split())
lists = list(map(int,input().split()))

lists.sort()

count = 0

for i in range(len(lists)-1):
    for j in range(i+1,len(lists)):
        if lists[i]!=lists[j]:
            count+=1
print(count)

#동빈이의 풀이(내것보다 시간 복잡도가 줌)
n,m = map(int,input().split())
data = list(map(int,input().split()))

array = [0] * 11
for x in data:
    array[x] += 1
]
result =  0
for i in range(1,m+1):
    n-= array[i]
    result += array[i] * n