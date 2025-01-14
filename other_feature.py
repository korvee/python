#集合解析,列表语法[<expression> for item list if <condition> ]
#set和字典也是可以的，中括号替换成大括号就可以，字典需要指明key和value两个值
list1 = [1,2,3,4]
map1 = {"a":1,"b":2}
set1 = {3,2,4}
# print([x for x in list1 if x >1])
#map也是可迭代对象，只是字典迭代器只返回键，不返回值。但如果想用这种方式过滤字典，也是很简单的，表达式和条件部分都可以通过键访问值，也可以返回一个字典对象
#print({x: map1[x] for x in map1 if map1[x] > 1})
#想迭代键和值，可以使用字典的item方法
# for key,value in map1.items():
#     print(key,":",value)

#可迭代对象，包含__iter__方法，可返回一个迭代器
#迭代器，包含__next__方法，每次返回一个元素，直到末尾引发stopiteration异常
#迭代器只有一个next方法，所以只能用迭代器前进，没办法重置迭代器或获取以前的元素
#迭代器对象和迭代器不必是分开的，可以创建一个包含iter和next方法的对象，它就同时是迭代器对象和迭代器
list1 = [1,2,3,4,5]
#phthon内置的迭代器对象主要包括列表，集合，字典，元组，范围，字符串

#自定义迭代器，只需要实现iter，next方法以及在迭代结束时抛出stopiteration异常即可
class EvenNumbers:
    last = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.last += 2
        if self.last > 20:
            raise StopIteration
        return self.last
even_numbers = EvenNumbers()
# for num in even_numbers:
#     print(num)

