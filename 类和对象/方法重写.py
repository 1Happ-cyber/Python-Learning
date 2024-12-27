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
    def show(self):
        super().show()
        print("student show")

st = Student("张三", 20, 100)
st.show()