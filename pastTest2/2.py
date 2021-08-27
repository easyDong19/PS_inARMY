p = input()
result = 0
for word in p:
    if result == 0 :
        result += int(word)
    elif word == 0 or word ==1:
        result += int(word)
    else:
        result *= int(word)

print(result)