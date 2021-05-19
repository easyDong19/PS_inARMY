T = int(input())
lists = []
for i in range(T):
    lists.append( ( input().split() ) )

results = []
for list in lists:
    num = float(list[0])
    for i in list:
        if i == '@':
            num *=3
        elif i == '%':
            num +=5
        elif i == '#':
            num -=7
    results.append(num)

for result in results:
    print('%.2f' % result)
        
    
    
    