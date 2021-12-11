vowels = ['a','e','i','o','u']

while 1:
    count = 0
    x = input()
    x = x.lower()
    if x == "#": break
    for i in x:
        if i in vowels: count+=1
    
    print(count)