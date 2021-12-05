import sys
read = sys.stdin.readline

x,y,w,h = map(int,read().split())
print(min(h-y,y,x,w-x))
