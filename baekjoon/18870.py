n = int(input())
origin = list(map(int,input().split()))
data = sorted(list(set(origin))) #중복제거

dic = {data[i]:i for i in range(len(data))}
for i in origin:
    print(dic[i], end= ' ')

