T = int(input())
A = 300
B = 60
C = 10

T_ = T
A_ = T//A
T = T%A
B_ = T//B
T = T%B
C_ = T//C

if A_*A+B_*B+C_*C==T_:
    print(A_,B_,C_)
else:
    print(-1)


