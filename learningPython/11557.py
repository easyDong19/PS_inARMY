n = int(input())

mosts = []
for _ in range(n):
    Univ = int(input())
    lists = []
    for i in range(Univ):
        a,b = input().split()
        lists.append( (a,int(b)) )

    lists.sort(key = lambda x:-x[1])
    mosts.append(lists[0][0])

for i in mosts:
    print(i)

   


        
