#generator는 가지고 있는 값들을 전부 넘겨준 다음에는 
#더이상 값을 기억하지 않아서 메모리를 절약함

my_gen = (i for i in range(10000))
print(sum(my_gen))
