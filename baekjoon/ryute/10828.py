import sys
stack = []

n = int(input())
while(n>0):
    n-=1
    oper = sys.stdin.readline().split()
    
    if oper[0] == "push":
        stack.append(oper[1])
    if oper[0] =="pop":
        print(stack.pop() if len(stack)>0 else -1)
    if oper[0] == "size":
        print(len(stack))
    if oper[0] == "empty":
        print(1 if len(stack)==0 else 0)
    if oper[0] == "top":
        print(-1 if len(stack)==0 else stack[-1])
        
        
    