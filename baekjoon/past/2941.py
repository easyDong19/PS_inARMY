text = input()
change = ['c=', 'c-','dz=','d-','lj','nj','s=','z=']

for i in change:
    text = text.replace(i,'a')
print(len(text))