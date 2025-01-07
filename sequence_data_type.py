#python三种内置序列数据类型，tuple，list/set，dictionary
def tuple_test():
    my_number = (3,2,5,4)
    my_number2 = 3,2,5,4
    my_mixed_tuple = ('hello worrd',True,3)
    my_number3 = (*my_number,*my_number2)#前导*操作符将列表解压缩为单个元素，这个解包操作适用于所有可迭代类型
    #另外一种解包方法，多重赋值
    person = ('elon',25,True)
    name,age,registerd = person
    #解包元组可以用于从python函数返回多个值
    def get_user_info():
        user_name = 'jack'
        user_age = 25
        return user_name,user_age
    user_name,user_age = get_user_info()
    # print(user_name,user_age)
    user_info = get_user_info()
    # print(user_info[0],user_info[1])
    #tuple和list的主要区别是tuple不可变，list可变，定义tuple后，不能添加或删除值，tuple的这个特性可作为对不可变数据的一个保护
    #tuple于set相比，set中的数据是不可重复的，set是一个很好的消除重复的工具

    #可将tuple转换为list或set集合，然后就可对序列进行修改了
    list1 = [*user_info]
    set1 = set(user_info)
    set2 = {*user_info}
    #像大所述python对象一个，元组也包含一个__str__方法，通过该方法可将元组打印为字符串，当然无需显示这样做

#list是python中最常用的数据结构，除了列表，还可被用作栈或队列
def list_test():
    #列表创建
    my_list1 = [1,2,3]
    my_list2 = []
    my_list3 = [1,'elon',{'age':39}]
    #使用构造函数list，可以将任何可迭代对象转换为list
    # print(type(list(range(2,5))))
    #列表访问,通过位置下标访问
    # print(my_list1[0])
    # print(my_list1[-1])#从后往前获取元素，-1获取最后一个元素
    #列表嵌套
    nested_list = [[1,2],[3,4]]
    # print(nested_list[0][0])#和多维数组一样访问
    #添加和删除元素
    my_list1.append(4)
    # print(my_list1)
    #合并两个列表
    my_list4 = my_list1 + my_list3
    # print(my_list4)
    my_list1.extend(my_list3)#扩展my_list1，将my_list3的内容添加到my_list1中
    # print(my_list1)
    #pop方法弹出元素，可选择弹出开头，末尾或者中间位置的元素，list的pop和append方法结合使用就可以实现堆栈和队列了
    pop_list = [1,2,3,4,5]
    # print(pop_list.pop(),pop_list)
    # print(pop_list.pop(0),pop_list)
    #del方法可以删除列表中的元素，列表以及python中的任何对象，并且可以递归执行。
    # 删除内容可以让python知道可以释放被删除对象的内存，对不在使用的大对象进行删除时有益的
    # del(pop_list[0])
    # del(pop_list)
    #使用remove方法从列表中删除特定值，使用clear方法清除列表中的值
    pop_list.remove(2)
    # print(pop_list)
    pop_list.clear()
    # print(pop_list)
    #删除列表中重复项的技巧，将列表转为集合，再转回列表
    list1 = [1,2,3,3,4]
    set1 = set(list1)
    # list1 = list(set1)
    list1 = list(set(list1))
    # print(list1)
    #其他可用的方法
    list2 = [1,2,3,4,5,5,5]
    list2[0] = 7#替换元素
    len(list2)#获取list长度
    # print(list2.count(1),list2.count(5))#统计元素出现的次数
    list3 = ['jack','leo','leo']
    # print(list3.count('jack'),list3.count('leo'))#字符串也可用
    #检查项是否在列表中
    # if 'jack' in list3:
    #     print('jack is in list3')
    # print(list3.index('leo'))#检查元素在列表中的索引
    # print(list3.index('leo',2))#从指定位置开始查找
    #排序，要求列表中的元素类型一致，不一致会报错
    sort_list = [6,4,9,2,90]
    sort_list.sort()#就地升序排列
    sort_list.sort(reverse=True)#就地降序排列
    sorted_list = sorted(sort_list)#不修改原列表，返回升序排序后的列表
    sorted_list = sorted(sort_list,reverse=True)#不修改原列表，返回降序排序后的列表
    sort_list = ['a',1,'c',3]
    # print(sort_list.sort())#不能包含不同类型的对象，数字和字符串比较会报错
    sort_list = [(3,4),(4,9),(5,3)]#这样也可以排序，类型需要一致
    #切片,语法list[start:stop:step]，范围为左闭右开
    slice_list = [1,2,3,4,5,6]
    # print(slice_list[0:3]) #取[0,4)的元素
    # print(slice_list[:3])#不指定开始位置，默认从0开始
    # print(slice_list[4:])#从位置5开始，取到最后
    # print(slice_list[::2])#默认步长为1，及考虑所有元素，步长为2意味着每次跳过一个元素
    #反转列表
    reverse_list = [1,2,3,4]
    # print(reverse_list.reverse(),reverse_list)#原地反转列表
    reverse_list2 = reverse_list[::-1]#等效于reverse_list[-1:-5:-1]，todo这个负数步长不知道怎么理解
    # print(reverse_list2)
    # for i in reversed(reverse_list):#最后是使用reversed方法创建一个反向迭代器，这个操作消耗资源很少，对大列表进行反转优先使用这个
    #     print(i)
    #列表解析，语法[<expression> for item in list if <condition>]
    #python没有列表解析也不会影响它的功能，列表解析可以使用map和reduce编程式函数或者for循环代替，知识没列表解析简洁
    result = [x+10 for x in range(1,10) if x % 2 == 0]#对于迭代返回结果，如果为偶数，就将迭代结果+10放入返回列表中
    # print(result)
    result = [[j for j in range(3)] for i in range(3)]#i in range(3)循环3次，每次循环返回j for j in range(3),而该表达式返回[0,1,2]，所以结果就是三个[0,1,2]了
    print(result)

#python set集合，set只包含唯一值，set是无序的
def set_test():
    set1 = set()
    set1.add(1)
    set1.add('leo')
    set1.update([3,4,'jack'])#update方法添加一个可迭代对象，实现一次添加多个值
    # print(set1)
    #集合解析
    my_set = {x for x in 'Hi, my name is jack ...' if x in 'ni'}#返回结果为i和n，todo in后面放入连续的多个字符，也会拆开，就像sql里的in('n','i')一样执行
    my_set = {x for x in 'Hi, my name is jack ...' if x not in ' ,.'}#返回除了空格点顿号以外的其他字母
    # print(my_set)
    #set的使用场景1）去除重复项2）成员资格测试（判断元素是否在唯一名单中）3）还可以执行数学上的交集差集并集等集合操作
    set1 = {1,2,3,4}
    set2 = {3,4,5,6}
    set3 = {1,2}
    print(set1-set2)#差集，a减去a和b重合的部分
    print(set1 & set2)#a和b差集
    print(set3 < set1)#判断set3是否是set1的子集，>则是判断是否为超集，默认是真子集（子集且不等于），<=可以用来判断子集
    print(set1|set2)#a和b的合集
    #几乎所有的集合运算都可以用方法来代替issubset(),issuperset(),union()，intersection（），difference（）
    #命名方法的好处是参数可以接受任意类型的可迭代对象，省去了类型间的转换
    #集合没有顺序，不能使用集合索引访问集合元素

#python字典，也称关联数组
def dictionary_test():
    phone_numbers = {'jack':'3265','petter':'9870'}
    phone_numbers['leo'] = '8737'#添加元素
    del(phone_numbers['jack'])#删除元素
    result = phone_numbers.get('petter1')#使用get方法的好处是，key不存在时返回none而不会报错
    #字典的key值要求可散列（对象在创建后散列值不变，元组是可以作为键的），可变类型（如字典，列表，集合）不行，将抛出错误
    # 字典解析，expression需要指定键值
    result = {x : x**2 for x in (1,2,3,4) if x < 4}
    names = ['jack','leo','petter']
    phone_numbers = dict.fromkeys(names,None)#fromkeys函数接收可迭代对象作为键，生成字典
    #json字符串解析为字典
    jsonStr = '{"name":"leo","age":24,"married":true}'
    import json
    result = json.loads(jsonStr)
    # print(type(result),result)
    #检查字典中是否存在键
    # if 'name1' in result:
    #     print('yes')
    #字典视图对象,keys和values方法返回键和值的列表
    result1 = result.keys()
    # print(type(result1),result1)
    #items方法返回一个可迭代的视图对象，提供键和值
    # for key,value in result.items():
    #     print(key,':',value)
    list(result)#返回按照插入顺序排序的所有键的本地列表

    phone_numbers1 = {'jack':'3265','petter':'9870'}
    phone_numbers2 = {'leo':'8967','jack':'5323'}
    #两种方式合并两个字典
    merged = phone_numbers1|phone_numbers2
    merged = {**phone_numbers1,**phone_numbers2}
    print(merged)


 








dictionary_test()