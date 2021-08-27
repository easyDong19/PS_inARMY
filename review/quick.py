import random

#랜덤 리스트
randLists = []

for _ in range(10):
    x = random.randint(1,10)
    randLists.append(x)

print(randLists.sort())

def quick(lists,start,end):
    if start>=end:
        return
    pivot = start
    left = start+1
    right = end

    #왼쪽 인덱스가 오른쪽 인덱스보다 작을동안
    while left <= right:
        #피벗보다 값이 큰 레프트 인덱스 구하기
        while left < end and lists[left]<lists[pivot]:
            left+=1
        while right > start and lists[right]>lists[pivot]:
            right-=1
        
        #왼쪽 오른쪽이 엇갈렸을 경우
        if left>right:
            lists[pivot],lists[right] = lists[right],lists[pivot]
        else:
        #아닐 경우
            lists[left],lists[right] = lists[right],lists[left]
    
    quick(lists,start,right-1)
    quick(lists,right+1,end)


