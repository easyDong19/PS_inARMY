#zip 예시
name = ['merona', 'gugucon']
price = [500,1000]

z = zip(name,price)
print(list(z))

for n, p in zip(name, price):
    print(n, p)

#딕셔너리 setdefault 메서드


data = ["BTC", "BTC", "XRP", "ETH", "ETH", "ETH"]
#set집합 중복을 제거함
for k in set(data):
    count = data.count(k)
    print(k, count)

#딕셔너리 컴프리헨션
icecream = {k:v for k, v in zip(name,price)}
icecream = {k:v for k, v in zip(name,price) if v < 1000}


