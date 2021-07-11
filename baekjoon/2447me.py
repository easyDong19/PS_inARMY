# n = int(input())
# def star(n):
#     global Map
    
#     if n==3:
#         Map[0][:3] = Map[2][:3] = [1] *3
#         Map[1][:3] = [1,0,1]
#         return

#     a = n//3
#     star(n//3)
#     for i in range(3):
#         for j in range(3):
#             if i==1 and j==1:
#                 continue
#             for k in range(a):
#                 Map[i*a+k][j*a:(j+1)*a] = Map[k][:a]



# Map = [[0 for _ in range(n)] for _ in range(n)]
# star(n)

# for i in Map :
#     for j in i :
#         if j :
#             print('*', end = '')
#         else :
#             print(' ', end = '')
#     print()
n = int(input())
a = "*"
while n>1:
    x = [i*3 for i in a]
    y = [i + ' '*len(i) + i for i in a]
    a = x+y+x
    n = n//3
    

print('\n'.join(a))