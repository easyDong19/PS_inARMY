A = int(input())
B = int(input())
C = int(input())

S = list(str(A*B*C))
number = [0]*10

for i in S:
    number[int(i)]+=1

for i in number:
    print(i)