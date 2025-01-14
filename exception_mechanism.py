#python的顶层异常对象是BaseException，except后留空等同于捕获顶层异常
def base_exception_test():
    try:
        3/0
    except:
        print('divide zero error')
#可以使用异常作为一块代码的判断，比如判断多个key是否在字典中存在。异常在python中并不会使用很多资源，大量的比较比捕获单个异常要慢

#自定义异常类，继承了Exception的所有属性和方法
class UserNotFoundError(Exception):
    pass
#主动抛出异常
def fetch_user():
    user = None
    if user == None:
        raise UserNotFoundError('user not in database')

#导入traceback模块打印错误堆栈信息
import traceback   
try:
    fetch_user()
except UserNotFoundError as e:
    print('there is an error',e)
    traceback.print_exc()