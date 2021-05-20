a_ = []
b_ = []
for _ in range(3):
    a,b = map(int,input().split())
    a_.append(a)    
    b_.append(b)

x = 0
y = 0
for i in range(3):
    if a_.count(a_[i]) == 1:
        x = a_[i]   
    if b_.count(b_[i]) == 1:
        y = b_[i]
print(x,y)