#强制关键字参数
#1）不必按照顺序指定参数2）参数名有见名知意的效果
def f(*,a,b):
    print(a,b)

# f(a=1,b=2)#这样就只能通过指定参数名调用了
arg = {"a":1,"b":2}
# f(**arg)#也可以传入字典对象调用强制关键字函数

def f2(a,b,c):
    print(a,b,c)

list1 = [1,2,3]
# f2(*list1)#使用*可以解包列表


#装饰器函数todo好简略
def print_argument(func):
    def wrapper(the_number):
        print("Argument for", func.__name__, "is", the_number)
        return func(the_number)
    return wrapper
@print_argument
def add_one(x):
    return x + 1
# print(add_one(1))

#python的匿名函数，函数可以接受函数作为参数，只能执行一次时，可以通过lambda直接将函数实现传递给函数，省略声明的过程
numbers = [1,2,3,4]
def plus2(x):
    return x+2

#下面这两种是等价的
# times_two = map(lambda x:x+2,numbers)
times_two = map(plus2,numbers)
# print(list(times_two))