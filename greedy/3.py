S = input()

seq = S[0]
a = []
Str = ""

for i in S:
    if i==seq:
        Str +=i
    else:
        a.append(Str)
        seq = i   
        Str = ""
        Str +=i

a.append(Str)

count_1=0
count_0=0
for i in a:
    if '1' in i:
        count_1+=1
    else:
        count_0+=1

print(min(count_1,count_0))


#동빈의 풀이
data = input()
count0 = 0  #전부 0으로 바꾸는 경우
count1 = 0  #전부 1로 바꾸는 경우

if data[0] == '1':
    count0 +=1
else:
    count1 +=1

#두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 +=1


print(min(count1,count0))
