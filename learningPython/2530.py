a,b,c= map(int,input().split())
n = int(input())

hour = n//3600
minn = n//60
sec = n%60

a = a + hour%24
b = b + minn%60
c = c + sec

if c>=60:
    c-=60
    b+=1
if b>=60:
    b-=60
    a+=1
if a>= 24:
    a -=24

print(a,b,c)