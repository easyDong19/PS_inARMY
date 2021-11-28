
MAX = 10001
prime = [1] * MAX 
prime[0] = 0
prime[1] = 0
for i in range(MAX):
    if prime[i] == 1:
        for not_prime in range(2 * i, MAX, i):
            prime[not_prime] = 0


MAX = 100
prime = [1] * MAX
prime[0] = 0; prime[1] = 0
for i in range(MAX):
    if prime[i] == 1:
        for not_prime in range(2*i,MAX,i):
            prime[not_prime] = 0
