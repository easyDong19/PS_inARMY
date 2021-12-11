import sys
#알파벳 갯수 세기
str = sys.stdin.read()

alphabet = [0] * 26

for i in str:
    if i.islower():
        alphabet[ord(i)-97]+=1

maxx = max(alphabet)
for i in range(26):
    if alphabet[i] == maxx:
        print(chr(i+97), end ="")
    