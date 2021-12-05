n,m,k = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

first = data[-1]
second = data[-2]

result = 0
#몇번 나눠질 수 있는가
target = m // (k+1)
mod = m % (k+1)
result = first * k * target + target*second + mod * first

print(result)

