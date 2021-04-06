#시간 복잡도 O(N^2) 최선의 경우 O(N) 
#정렬이 거의 되있는 경우 퀵정렬보다 빠름 
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)            
