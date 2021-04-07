def binary_search(array,target,start,end):
    if start>end:
        print('no')
        return None
    mid = (start+end)//2
    if array[mid] == target:
        print("yes")
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else: return binary_search(array,target,mid+1,end)


    
n  = int(input())
array = list(map(int, input().split()))
m = int(input())
target = list(map(int,input().split()))

array.sort()

for i in target:
    binary_search(array,i,0,n-1)