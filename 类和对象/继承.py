# Python中一个子类可以继承N多个父类
# 一个父类也可以有N多个子类
# 如果一个类没有继承任何类，那么默认继承object类


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("eat")

    def show(self):
        print("show")


class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

st = Student("张三", 20, 100)
st.show()