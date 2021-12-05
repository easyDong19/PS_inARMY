n, k = map(int,input().split())
#k로 나눠질 때까지의 수 확인
count = 0
target = n%k
n = n-target
while n>1:
    n//=k
    count+=1
count += target 

print(count)