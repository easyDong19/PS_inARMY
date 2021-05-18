a,b = map(int,input().split())
c = int(input())

sum = b+c
if sum >= 60:
    a = a+(sum//60)
    sum = sum%60
    if a >= 24:
        a = a-24

print(a,sum)

