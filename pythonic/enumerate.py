data = [1,2,-4,-3]
for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0
    
#반복문 사용시 몇 번째 반복문인지 
#확인이 필요할 때 사용
#인덱스 번호와 컬렉션 원소 -> tuple
data = [1,2,-4,-3]
for idx, num in enumerate(data):
    if num<0:
        data[idx] = 0
