def my_write():
    lst = ['1', '2', '3', '4', '5']
    with open('test.csv', 'w') as f:
        f.write(','.join(lst))



def my_read():
    with open('test.csv', 'r') as f:
        s=f.read()
        lst=s.split(',')
        print(lst)

def my_write_table():
    lst = [['a', 'b', 'c'], ['1', '2', '3'], ['4', '5', '6']]
    with open('test_table.csv', 'w') as f:
        for item in lst:
            f.write(','.join(item))
            f.write('\n')

def my_read_table():
    data=[]
    with open('test_table.csv', 'r') as f:
        lst=f.readlines()
        for line in lst:
            new_list=line[:len(line)-1].split(',')
            data.append(new_list)

    print(data)
if __name__ == '__main__':
    my_write()
    my_read()
    my_write_table()
    my_read_table()
