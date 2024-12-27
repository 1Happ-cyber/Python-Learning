# 类属性：直接定义在类内，方法外的变量
# 实例属性：定义在_init_方法中，使用self大点的变量
# 实例方法：定义在类中的函数，而且自带参数self
# 静态方法：用装饰器@staticmethod装饰的方法
# 类方法：用装饰器@classmethod装饰的方法


class Student:
    scool = '100'
    def __init__(self,xm,age):
        self.name = xm#左侧是实例属性，右侧是形参
        self.age = age
    def show(self):
        print(self.age)
        print(self.scool)
    @classmethod
    def get_school(cls):
        #不让调用实例属性以及实例方法
        return cls.scool

    @staticmethod
    def add(a, b):
        #不让调用实例属性以及实例方法
        print('%d + %d = %d' % (a, b, a+b))

#创建对象
#实例属性/方法，使用对象名打点调用
ck = Student('ck',23)
print(ck.age)
#类属性/方法，使用类名打点调用
print(Student.scool)
#静态方法，使用类名打点调用
Student.add(1,2)
#动态绑定一个实例属性
ck.sex = '男'
print(ck.sex)
#动态绑定实例方法
def eat():
    print('eat')
ck.eat = eat
ck.eat()


