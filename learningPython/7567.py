#그릇이 같은 모양이면 5
#그릇이 다른 모양이면 10
#처음 그릇 바닥 10

bowl = input()
h=10
for i in range(0,len(bowl)-1):
    if bowl[i] == bowl[i+1]:
        h+=5
    else: h+=10
print(h)

    
