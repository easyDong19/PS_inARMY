h, m = map(int, input().split())

m = m-45 
if m < 0:
  if h>0:
    h-=1
  else:
    h=23
  m = 60 + m
print(h,m)
