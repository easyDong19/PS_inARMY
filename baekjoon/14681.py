#규칙을 찾는 것이 중요하다
#출처 https://leedakyeong.tistory.com
n = int(input())
arr = [["*"] *n for _ in range(n)]

v = n
cnt = 0
while v!=1:
    v/=3
    cnt+=1

#
for cnt_ in range(cnt):
    idx = [i for i in range(n) if (i//3 ** cnt_) % 3 == 1]
    for i in idx:
        for j in idx:
            arr[i][j] = ' '

# for row in arr:
#     for i in row:
#         print(i,end='')
#     print('')

print('\n'.join([''.join([str(i) for i in row]) for row in arr]))