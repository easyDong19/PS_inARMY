lists = []
for _ in range(5):
    score = int(input())
    if score < 40: score = 40
    lists.append(score)

print(sum(lists)//5)