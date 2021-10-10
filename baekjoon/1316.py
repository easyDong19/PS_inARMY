n = int(input())
p = []
count = 0
for _ in range(n):
    check = [0] * 26
    word = input()
    before = ''
    for i in word:
        if before == i:
            continue
        check[ord(i)-97]+=1
        before = i
    if max(check) <= 1:
        count+=1

print(count)
        
