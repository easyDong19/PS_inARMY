data = input()

count_1 = data.count("1")
count_0 = data.count("0")

change = "1" if count_1<=count_0 else "0"
result = 0
before = data[0]
#적은 숫자를 뒤집어주면 됨
for i in data[1:]:
    if i == change and before!=i:
        result+=1
    before = i

        
print(result)
        