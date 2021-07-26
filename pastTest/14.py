from itertools import permutations

def solution(n, weak, dist):
    #길이를 2배로 늘려서 원형 -> 일자
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 #투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    #0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        #친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist,len(dist))):
            count = 1 #투입할 친구 수
            #해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count-1]
            #시작 점부터 모든 취약 지점 확인
            for index in range(start, start + length):
                #점검할 수 있는 위치를 벗어 나는 경우
                if position < weak[index]:
                    count+=1 # 새로운 친구를 투입할
                    if count > len(dist): #더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer
                    

