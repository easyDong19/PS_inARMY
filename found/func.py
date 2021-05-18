#위치 가변 인자 
def foo(*args):
    print(args)

foo(1,2,3)
foo(1,2,3,4)

#키워드 가변 인자
def foo(**kwargs):
    print(kwargs)

foo(a=1,b=2,c=3)
