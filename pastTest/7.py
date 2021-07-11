N = list(input())
sum_left = 0
sum_right = 0

for idx, n in enumerate(N):
    if idx < int(len(N)//2):
        sum_left += int(n)
    else:
        sum_right += int(n)

if sum_left == sum_right:
    print("LUCKY")
else:
    print("READY")