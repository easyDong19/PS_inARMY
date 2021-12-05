n,m = map(int,input().split())
ball = list(map(int,input().split()))

# #모든 가능한 경우
# possible = int((n-1)/2 * n)
# #무게가 같은 볼링공을 고르는 경우
# same = 0
# for i in range(1,m+1):
#     count = ball.count(i)
#     if count>1:
#         same += int((count-1)/2 * count)


# print(possible-same)

array = [0] * 11
for x in ball:
    array[x] += 1
    
result = 0
for i in range(1,m+1):
    n-= array[i]
    result += array[i] * n