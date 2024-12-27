class FatherA():
    def __init__(self, name):
        self.name = name

    def showA(self):
        print("FatherA:", self.name)

class FatherB():
    def __init__(self, age):
        self.age = age

    def showB(self):
        print('FatherB:', self.age)

class son(FatherA, FatherB):
    def __init__(self, name, age, gender):
        self.gender = gender
        FatherA.__init__(self, name)
        FatherB.__init__(self, age)

son= son('zhangsan', 20, 'male')
son.showA()
son.showB()
