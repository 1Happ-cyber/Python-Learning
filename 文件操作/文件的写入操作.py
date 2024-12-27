
def mywrite(s):
    file = open('test.txt', 'a',encoding='utf-8')
    file.write(s)
    file.write('\n')
    file.close()

def my_write_list(file, lst):
    f=open(file,'a',encoding='utf-8')
    f.writelines(lst)
    f.close()


if __name__ == '__main__':
    lst= ['\twelcome to python\t', '伟大中国梦\t']
    my_write_list('test.txt', lst)
    # mywrite("welcome to python")
    # mywrite("伟大中国梦")