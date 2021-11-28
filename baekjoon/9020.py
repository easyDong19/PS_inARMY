import sys
read = sys.stdin.readline

def goldBache(k, prime, MAX):
    half = k // 2 
    for val in range(half, MAX):
        if prime[val] and prime[k - val]:
            return val
    return -1


MAX = 10001
prime = [1] * MAX 
prime[0] = 0
prime[1] = 0
for i in range(MAX):
    if prime[i] == 1:
        for not_prime in range(2 * i, MAX, i):
            prime[not_prime] = 0

n = int(input())
while(n > 0):
    k = int(read())
    pair_1 = goldBache(k, prime, MAX)
    pair_2 = k - pair_1
    print("{} {}".format(pair_2, pair_1))
    n -= 1