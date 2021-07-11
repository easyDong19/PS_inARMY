S = list(input())

alpha = [x for x in S if x.isalpha()]
number = [x for x in S if x.isdigit()]
number = map(int,number)
alpha.sort()

for i in alpha:
    print(i, end='')

print(sum(number))
