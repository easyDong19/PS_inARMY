# n = int(input())
# lists = list(map(int,input().split()))

# lists.sort(reverse=True)

# group = lists[0]
# check = 1
# sum = 0
# for i in range(len(lists)):
#     if check == 0:
#         group = lists[i]
#         check = 1

#     group -= 1
#     if group==0:
#         sum+=1
#         check = 0
    
        
# print(sum)

n = int(input())
data = list(map(int,input().split()))
data.sort
result = 0
count = 0

for i in data:
    count+=1
    if count>=i:
        result +=1
        count = 0

print(count)