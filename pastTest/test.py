a = 0
def recursive(count):
    global a
    if count==3:
        a+=1
        print(a)
        return 

    for i in range(3):
        for j in range(3):   
            count+=1
            recursive(count)
            count-=1

print(recursive(0))