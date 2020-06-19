'''
@describle: 链接：https://www.nowcoder.com/questionTerminal/bb306a3111574d4c8c48715c7b8bce96?mutiTagIds=239_645&orderByHotValue=1
来源：牛客网

按要求分解字符串，输入两个数M，N；M代表输入的M串字符串，N代表输出的每串字符串的位数，不够补0。例如：输入2,8， “abc” ，“123456789”，则输出为“abc00000”,“12345678“,”90000000”
@author: kuochung
@email: jxgxzgc@163.com
@datetime: 20200402
'''


def str_split(m, n, *args):
    result_str = []
    tmp = ''
    for item in args:
        item = tmp + item
        if len(item) <= n:
            tmp = item + (n-len(item))*'0'
            result_str.append(tmp)
            tmp = ''
        else:
            iters = len(item) // n
            i = 0
            for iter in range(iters):
                result_str.append(item[i:i+n])
                i += n + 1
            tmp = item[iters*n:]
            if item == args[-1]:
                result_str.append(tmp+(n - len(item) % n)*'0')
    return result_str


if __name__ == '__main__':
    print(str_split(2, 8, 'abc', '1234567892345720842038429048'))