s = int(input())

i=1
count = 0
while(s!=0):
   s-=i 
   if(s<0): break
   i+=1
   count+=1

print(count)