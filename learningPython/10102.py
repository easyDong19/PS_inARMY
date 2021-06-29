n = int(input())
string = input()

A = string.count("A")
B = string.count("B")

if A-B>0: print("A")
elif A-B<0: print("B")
else: print("Tie")
