n = int(input())

def Fibo(n):
    if n==1: return 1
    if n==0: return 0

    return Fibo(n-1) + Fibo(n-2)

print(Fibo(n))
