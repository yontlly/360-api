
def my_decorator(func):
    def wrapper(*args,**kwargs):
        print('wrapper of decorator')
        func(*args,**kwargs)
        print("hhh")
    return wrapper

@my_decorator
def greet(a,b):
    print('我输入的内容是{} {}'.format(a,b))

greet(1,2)