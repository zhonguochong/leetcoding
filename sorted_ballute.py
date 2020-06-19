'''
@Author: zhonguochong
@Date: 2020-06-18 09:00:00
@LastEditTime: 2020-06-18 10:03:49
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /studyleetcode/sorted_ballute.py
'''
import sys
import random


class CheckOutException(Exception):
    def __init__(self):
        pass


class SortedBullute():
    def __init__(self):
        self.dic = {}  # 存放不同气球颜色和其相应的个数
        self.choosed_pool = []  # 存放待排列的气球颜色集
        self.result = []  # 相同颜色气球不相邻的排列组合
        print('分别输入气球颜色和数量[eg. white 1][连续按两个Enter健结束输入]:')
        try:
            while True:
                line = sys.stdin.readline()
                if line == '\n':
                    break
                self.dic[line.split()[0]] = int(line.split()[-1].strip('\n'))
                self.choosed_pool.append(line.split()[0])
            if max([num for num in self.dic.values()]) < (sum([num for num in self.dic.values()]) + 1) // 2:  # 判断输入数据不符合排列组合需求的情况
                raise CheckOutException()
        except CheckOutException as result:
            print('CheckOutError: 输入数据不符合排列组合需求!')
            sys.exit()
    
    def __call__(self):
        tmp = None  # 存储上一个排列的气球颜色
        while max(self.dic.values()) > 0:
            choosed_color = random.choice(self.choosed_pool)
            if choosed_color ==  tmp:
                continue
            tmp = choosed_color
            self.result.append(tmp)
            self.dic[tmp] -= 1
            # 判断tmp气球颜色是否全部排列完成
            if self.dic[tmp] == 0:
                self.choosed_pool.remove(tmp)
        return self.result
         
if __name__ == "__main__":
    print(SortedBullute()())