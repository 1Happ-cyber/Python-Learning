# 变量的赋值：实际还是指向同一个对象
# 浅拷贝：对象包含的子对象不拷贝，因此，源对象与拷贝对象会引用同一个子对象
# 深拷贝：使用copy模块的deepcopy函数，递归拷贝对象中的子对象,源对象与拷贝对象所有的子对象也不相同

class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk

cpu=CPU()
disk=Disk()
con=Computer(cpu,disk)
con1=con#变量的赋值
print(con,con.cpu,con.disk)
print(con1,con1.cpu,con1.disk)

#类的浅拷贝
import copy
con2=copy.copy(con)
#con2是新产生的对象，但其子对象cpu,disk与con相同
print(con2,con2.cpu,con2.disk)

#类的深拷贝
con3=copy.deepcopy(con)
#con3是新产生的对象，其子对象cpu,disk与con不同
print(con3,con3.cpu,con3.disk)

