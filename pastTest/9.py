
def solution(s):
    answer = len(s)
    #1개 단위부터 압축 단위를 늘러가며 확인
    for step in range(1,len(s)//2 +1):
        compressed = ""
        prev = s[0:step]
        count = 1
        #step 크기만큼 증가시키며 이전 문자열 과 비교
        for j in range(step,len(s),step):
            #이전 상태와 동일하다면 압축 횟수 증가
            if prev == s[j:j+step]:
                count+=1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                #j+step >= len(s) 넘어가도 파이썬은 인덱스 에러가 뜨지 않고
                #j부터 마지막 문자열까지 슬라이싱한다
                prev = s[j:j+step]
                count = 1

        #남아있는 문자열에 대해서 처리
        compressed += str(count) + prev if count>=2 else prev
        
        answer = min(answer,len(compressed))
    return answer

    #머릿속으론 알고리즘을 세웠으나 실제로 구현 능력이 부족하여 구현하지 못함
