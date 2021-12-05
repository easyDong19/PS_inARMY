a,b,v = map(int,input().split())

#마지막날은 밤에 안미끄러지니깐 v-b
#하루에 올라가는 양 a-b
#(v-b)//(a-b) 안나눠 떨어지면 +1
#(v-b-1) -1해준 이유: 나눠떨어지는 경우와 안나눠떨어지는 경우 구분없이 한 줄로 짤수 있음
result = (v-b-1)//(a-b) + 1
print(result)