from collections import namedtuple
#소괄호 없이 컴마로만 구분해도 튜플로 인식한다
a = 1, 2
b = (1,2)
print(a, type(a))
print(b, type(b))

#튜플 언패킹
data = (1,2,3)
n1, n2, n3 = data

#튜플언패킹 중 튜플의 일부값 하나의 변수로 묶어서 바인딩
scores = (1,2,3,4,5,6)
low, *other, high = scores

#함수값이 여러개 리턴하면 튜플로 패킹된후 튜플 객체 리턴
def foo():
    return 1, 2, 3

#언패킹과 함수 호출
def hap(num1, num2, num3, num4):
    return num1+num2+num3+num4

scores = (1,2,3,4)
result = hap(*scores)

#namedtuple
class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price 

Book = namedtuple('Book', ['title','price'])

