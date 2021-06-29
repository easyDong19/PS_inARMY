n = int(input())

chang = 100
sang = 100
for _ in range(n):
    a,b = map(int,input().split())
    if a-b>0:
        sang -=a
    elif a-b<0:
        chang-=b

print(chang)
print(sang)