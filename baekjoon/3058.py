T = int(input())
lists = []
for i in range(T):
    lists.append(tuple(map(int,input().split())))

for i in range(T):
    a = [x for x in lists[i] if x%2==0]
    print(sum(a),min(a))



    