n = int(input())
arr = list(map(int,input().split()))
arr.sort()

start = 0
end = n-1
result = -1
while start<=end:
    mid = (start+end)//2
    if arr[mid] > mid:
        end = mid-1
    if arr[mid] < mid:
        start = mid+1

    if arr[mid] == mid:
        result = mid
        break

print(result)
    