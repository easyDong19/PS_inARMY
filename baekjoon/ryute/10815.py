#이진탐색 binary_search
n = int(input())
sang = list(map(int,input().split()))
m = int(input())
data = list(map(int,input().split()))

#이진 탐색을 위한 정렬
sang.sort()

def binary_search(arr,start,end,target):
    result = 0
    
    while start<=end:
        mid = (start+end)//2
        if arr[mid] == target:
            result = 1
            break
        elif arr[mid] > target:
            end = mid-1
        elif arr[mid] < target:
            start = mid+1
    return result

for card in data:
    print(binary_search(sang,0,len(sang)-1,card),end=" ")

    
            
            
        
    
