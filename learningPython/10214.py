T = int(input())

for _ in range(T):
    a_= 0
    b_= 0
    for i in range(9):
        a,b = map(int,input().split())
        a_+=a
        b_+=b
    
    if a_>b_:
        print('Yonsei')
    elif a_<b_:
        print('Korea')
    else:
        print('Draw')

