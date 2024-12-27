import sys


def my_read(filename):
    f=open(filename,'w+', encoding='utf-8')
    f.write('hello world')
    f.seek(2)
    # s=f.read(2)
    # s=f.readline()
    # s=f.readline(2)
    s=f.readlines()

    print(s)
    f.close()

#图像的copy，而图像是二进制文件，所以需要用二进制方式打开
def copy(src, new_path):
    file1=open(src,'rb')
    file2=open(new_path,'wb')
    s=file1.read()
    file2.write(s)
    #先打开的后关
    file2.close()
    file1.close()

if __name__ == '__main__':
    src='./test.png'
    new_path='./test_copy.png'
    copy(src, new_path)
