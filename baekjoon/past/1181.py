n = int(input())
data = []
for _ in range(n):
    data.append(input())

data = list(set(data))
data.sort()
data.sort(key = lambda x: len(x))
for i in data:
    print(i)