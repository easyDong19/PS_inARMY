import heapq

def solution(food_times, k):
    if sum(food_times) <=k:
        return -1
    
    #남은 음식 개수
    food_list = len(food_times)
    q = []
    #(음식시간,인덱스)
    for i in range(food_list):
        heapq.heappush(q,(food_times[i],i+1))
    
    #음식 먹은 시간
    sum_time = 0
    #이전에 먹은 음식 시간
    previous_time = 0
    
    #음식먹은 시간 + 남은음식개수 * (음식시간-이전에 먹은 음식시간) < k
    while sum_time + (food_list * (q[0][0]-previous_time)) <=k:
        now = heapq.heappop(q)[0]
        sum_time += (now-previous_time) * food_list
        food_list -= 1
        previous_time = now
        
    #인덱스순으로 정렬
    q.sort(key= lambda x : x[1])
    return q[(k-sum_time) % food_list][1]


