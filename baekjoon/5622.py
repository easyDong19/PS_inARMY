dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
p = input()

result = 0
for word in p:
    for num in dial:
        if word in num:
            result += dial.index(num)+3
print(result)