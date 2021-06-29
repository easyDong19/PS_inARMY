n = int(input())
lists = []
for i in range(n):
    lists.append(int(input()))

if lists.count(1) > lists.count(0):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")

    