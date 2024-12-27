# 权限控制：
# 单下划线开头：表示受保护的成员，它只被内部使用，允许类本身以及子类访问，但是他实际可以被外部访问
# 双下划线开头：表示私有成员，它只被类本身使用，不允许子类访问，但是他实际可以被外部访问
# 首尾双下划线：特殊的方法

class Student():
    def __init__(self, name, age, gender):
        self._name = name#本类和子类可以访问
        self.__age = age#只有本类可以访问
        self.gender = gender

    def _fun1(self):
        print("fun1")

    def __fun2(self):
        print("fun2")

    def show(self):
        self._fun1()
        self.__fun2()
        print(self._name)
        print(self.__age)
    @property # 装饰器，将方法变成属性,一般与要修饰的私有属性名字一样
    def gender(self):
        return self.__gender
    @gender.setter #改成可写属性
    def gender(self,value):
        self.__gender = value

s = Student("张三", 20, "男")

s.gender = "女"
print(s.gender)#可以访问但是不可以修改
print(s._name)#可以访问，只是不推荐
# print(s._Student__age)