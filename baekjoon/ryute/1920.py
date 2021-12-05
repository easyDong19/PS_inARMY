#이분 탐색

n = int(input())
A = list(map(int,input().split()))
m = int(input())
M = list(map(int,input().split()))

A.sort()

def binary_search(arr, start, end, target):
    if start>end: return False

    mid = (start+end) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binary_search(arr,start,mid-1,target)
    elif arr[mid] < target: 
        return binary_search(arr,mid+1,end,target)

for i in M:
    if binary_search(A,0,len(A)-1,i): print(1)
    else: print(0)
