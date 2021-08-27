#생성자의 개수(1~10000)
constructor = [0]*10001

for i in range(1,10001):
    #숫자를 문자열로 변환
    result = 0 
    numbers = str(i)
    #N을 더해준다
    result += i
    #N의 자릿 수를 더해준다
    for digit in numbers:
        result += int(digit)
    if result<=10000:
        constructor[result]+=1

for i in range(1,10001):
    if constructor[i] == 0:
        print(i)
        
        