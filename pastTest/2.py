s = input()
lists = list(s)
print(lists)

sum = 0
for word in lists:
    word = int(word)
    if word ==0 or sum==0 or word ==1:
        sum += word
    else:
        sum *= word
    

print(sum)

