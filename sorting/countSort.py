#O(N+K)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8,3,3,2]

count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end= ' ')

