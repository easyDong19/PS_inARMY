#삽입정렬

n = int(input())
lists = []
for _ in range(n):
    lists.append(int(input()))

for i in range(1,len(lists)):
    for j in range(i,0,-1):
        if lists[j] < lists[j-1]:
            lists[j],lists[j-1] = lists[j-1],lists[j]

for i in range(n):
    print(lists[i])