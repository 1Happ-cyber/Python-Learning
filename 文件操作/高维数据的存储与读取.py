import json
lst=[{"name":"a","age":18},{"name":"b","age":20},
     {"name":"c","age":18},{"name":"d","age":20},
     {"name":"e","age":18},{"name":"f","age":20}]

s=json.dumps(lst,ensure_ascii=False,indent=4)#indent=4 缩进4个空格,ensure_ascii=False 正常显示中文
#从lst---->str
print(s)

#解码
lst2=json.loads(s)
print(lst2)