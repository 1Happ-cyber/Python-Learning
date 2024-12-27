# 文件：存储在计算机的存储设备的一组数据序列
# 不同类型的文件通过后缀名区分
# 文本文件：由于编码格式的不同，所占磁盘空间的字节数不同
# 二进制文件：没有统一的编码，文件直接由0/1组成


def my_write():
    file = open('test.txt', 'w', encoding='utf-8')
    file.write('hello world')
    file.close()

def my_read():
    file = open('test.txt', 'r', encoding='utf-8')
    print(file.read())

    file.close()

if __name__ == '__main__':
    my_write()
    my_read()