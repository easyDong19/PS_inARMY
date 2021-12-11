stick = [64] #처음에는 64cm만 가지고 있다
X = int(input())


#가지고 있는 막대중 길이가 가장 짧은 것을 절반으로 짜른다

while X != sum(stick):
    now_min = min(stick)
    stick.remove(now_min)
    half_stick = now_min//2
    stick.append(half_stick)
    if sum(stick) < X:
        stick.append(half_stick)
        
print(len(stick))