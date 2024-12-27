# 特殊属性：
# 例如：obg.__dict__,obg.__class__, obg.__doc__

class A:
    pass
class B:
    pass
class C(A, B):
    def __init__(self,name, age):
        self.name = name
        self.age = age
a=A()
b=B()
c=C('zhangsan', 20)
print(a.__dict__)#对象的属性字典
print(b.__dict__)
print(c.__dict__)

print(a.__class__)#对象的类
print(b.__class__)
print(c.__class__)

print(C.__base__)#类的基类(第一个)
print(B.__bases__)
print(C.__bases__)
