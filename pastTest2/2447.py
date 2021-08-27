n = int(input())

k = 3
star = ["*"]
while k<=n:
    line = [i * 3 for i in star]
    blank = [i+ " " * len(star) + i for i in star]
    star = line + blank + line
    k = k * 3

for i in star:
    print(i)