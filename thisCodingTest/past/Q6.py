import heapq

def solution(food_times, k):
    #전체음식을 먹는시간보다 k가 크다면 -1
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    
    sum_value = 0 #먹기위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식시간
    length = len(food_times)
    
    while sum_value + ((q[0][0]-previous) * length)<=k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous) * length
        length -= 1
        previous = now
    
    result = sorted(q,key = lambda x:x[1]) #음식 번호 기준
    return result[(k-sum_value)%length][1]