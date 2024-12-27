# 多态
# 即便不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用其中的方法。
# 在程序运行中根据变量所引用对象的数据类型，动态决定调用哪个方法。
# 不关心对象的数据类型，不关心类之间的继承关系，只关心对象的功能
# 只要不同的类中有同名的方法就可以多态。
class Person():
    def eat(self):
        print('eating')

class Dog():
    def eat(self):
        print('dog eating')

def func(obj):#其实obj可以看作是object
    obj.eat()
p = Person()
d = Dog()
func(p)
func(d)
print(dir(p))#其中很多不知道的函数其实就是继承自object类
# 其中：
# __init__创建时手动调用，用来初始化对象属性值
# __new__创建时自动调用，用来创建对象
# 其中先执行__new__，再执行__init__