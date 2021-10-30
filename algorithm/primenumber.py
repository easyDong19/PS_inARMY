import math

n = 1000 #2부터 1000까지 소수 판별
array = [True for i in range(n+1)]

for i in range(2,int(math.sqrt(n))+1):
    if array[i] == True: #i가 소수인 경우
        #i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1
        