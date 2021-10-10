n = int(input())
a='*'
while n > 1 :
    x = [i*3 for i in a]
    y = [i+' '*len(i)+i for i in a]
    a = x+y+x
    n = n//3
    print('\n'.join(a))