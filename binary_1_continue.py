'''
@Author: your name
@Date: 2020-06-23 14:07:32
@LastEditTime: 2020-06-23 15:13:38
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
3. 给定一个 int 数据 M，判断其二进制中 1 是否连续。比如 ： M = 120 -> 0111 1000 true;
M=184->1011 1000 false.实现函数 bool check(int M)。
@FilePath: /leetcoding/binary_1_continue.py
'''
def check(M):
    if M == 0 or abs(M) < 3:
        return False
    m = bin(M)
    if m.find('10', 2) >  0 and m.find('10', 2) < m.find('01', 2) :  # 找到不连续的字串
        return False
    else:
        return True

print(check(120))
print(check(184))
print(check(0))
print(check(-2))
print(check(9))


