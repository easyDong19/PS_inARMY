#이중 리스트
two_d_list = [[0 for _ in range(10)] for _ in range(10)]

#리스트 컴프리션 예시
squares = []
for i in range(10):
    squares.append(i*i)

squares = [i*i for i in range(10)]

#리스트 인덱싱 예시
lists = [i for i in range(10)]

#-는 역순
print(lists[-1])

#리스트 슬라이싱
#리스트 변수[시작인덱스:종료인덱스:step]
print(lists[1:3])

#인덱스 생략
print(lists[:3])
print(lists[3:])
print(lists[:])