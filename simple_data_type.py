#python中的string不可变，从内存层面来说，为string变量重新赋值会使它指向其他位置，而不会修改原位置的值
def string_test():
    string1 = 'hello'
    string2 = string1
    string1 = 'word'

#python中的小数是无界的（别超过机器内存就好，但这种情况在实际应用中无需考虑）
#str，int，float之间的转换
def int_cast():
    a = int('100')
    b = str(200)
    c = int(2.89)

#输出[2,40]之间的随机整数
def random_test():
    import random
    i = 0
    while i < 20:
        print(random.randint(2,40))
        i = i+1

#类型判断
def type_jungle():
    print(type(2))
    if isinstance(2,int):
        print('this is an int')

#python浮点数
def float_test():
    f1 = 1.25e-1
    f2 = float('3.65')
    f3 = 2.4
    f4 = 3
    # print(f1,f2,f3,f4)
    # #近似值,去尾方式，支持指定精度
    # print(round(f2))
    # print(round(f2,1))
    #数学库中导入向下和向上舍入方法，不支持指定精度，直接保存为整数
    from math import floor,ceil
    # print(floor(f2))
    # print(ceil(f2))
    #浮点数精度限制
    #结果0.30000000000000004，和js中的问题一样
    #一些小数实际上是无穷的，而用来存储小数的内存是有限的，所以许多数字是尽力而为的近似值
    print(0.1+0.2)
    #浮点数精度问题处理（浮点数的有限精度是浮点数在计算机内存中表示的基本属性，处理浮点数时，无法完全消除精度有限的问题）
    #python解决精度问题的方法
    #1）decimal模块，该模块提供了对十进制浮点运算的支持，缺点就是比float要慢很多
    #2）numPy模块
    #3）舍入浮点数，限制小数的位数





