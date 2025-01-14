#python是进行数据处理的理想语言，支持csv，json，xml等格式，通过外部库还可以处理比如yaml等格式

#python处理json数据，对象-》字典，数组-》列表，布尔整数浮点数字符串被对应到python对象的类型，null映射为none类型
# jsonstring = '{"name":"leo","age":25,"married":true}'
# import json
# person = json.loads(jsonstring)
# print(person['name'])

# import json
# person = {'name':'jack','age':25,'married':True}
# jsonstring = json.dumps(person,indent=4)
# print(jsonstring)

#从文件中读写json数据
# import json
# person = {'name':'jack','age':25,'married':True}
# jsonstring = json.dumps(person,indent=4)
# with open('C:/Users/王宏/notepad/test.txt','r') as f:
#     data = json.load(f)
#     print(data)
#第三方库jmespath用于从json中查询数据
# import jmespath
# persons = {"persons":[{"name":"elon","age":20},{"name":"jack","age":27},{"name":"king","age":50},{"name":"leo","age":50}]}
# res = jmespath.search('persons[*].age',persons)
# print(res)

#第三方库pyyaml用来解析yaml文件，yaml是易读的结构化数据，很适合充当配置文件
# import yaml
# with open('config.yaml') as f:
#     config = yaml.safe_load(f)
# print(config['host']['port'])

#内置的csv模块解析csv文件（无法读取excel文件）
#reader返回迭代器对象，不会一次读取整个文件
# path = 'C:/Users/王宏/notepad/'
# import csv
# with open(path+'csvtest.csv',newline='',encoding='utf-8') as f:
#     excelfile = csv.reader(f)
#     for row in excelfile:
#         print(row)

#pandas模块list list数据写入excle
# path = 'C:/Users/王宏/notepad/'
# import pandas as pd
# data = [['alice',23],['bob',30],['tom',23]]
# column_names = ['name','age']
# df = pd.DataFrame(data,columns=column_names)
# writer = pd.ExcelWriter(path+'test.xlsx',engine='xlsxwriter')
# df.to_excel(writer,sheet_name='first_sheet',index=False)
# writer.close()

#将json数据通过pandas模块写入excel，json-》字典数组，pandas可处理字典数据
# path = 'C:/Users/王宏/notepad/'
# persons = {"persons":[{"name":"elon","age":20},{"name":"jack","age":27,'married':False},{"name":"king","age":50,'childs':[{'name':'child1','age':10},{'name':'child2','age':11}]},{"name":"leo","age":50}]}
# import json
# import pandas as pd
# jsonstr = json.dumps(persons)
# res = json.loads(jsonstr)
# res1 = res['persons']
# print(res1)
# df = pd.DataFrame(res1)
# writer = pd.ExcelWriter(path+'test.xlsx',engine='xlsxwriter')
# df.to_excel(writer,sheet_name='first_sheet',index=False)
# writer.close()
