'''
@Author: your name
@Date: 2020-06-24 08:23:48
@LastEditTime: 2020-06-24 11:06:49
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
1. 某楼盘有 M 层（实际层数， M < 100），每层高度为 N。由于开发商比较迷信，楼层数字
带 4 的全部跳过（1 楼， 2 楼， 3 楼， 5 楼……没有 4 楼），隔壁老王坐电梯到了 X 层，
请问他在离地面多高的位置。请用代码实现此功能。
@FilePath: /leetcoding/compute_floor.py
'''
import sys


class MaxFloorException(Exception):
    def __init__(self, m):
        self.M = m


class FloorNumException(Exception):
    def __init__(self, x, m):
        self.X = x
        self.M = m


class Solution(object):
    def __init__(self, n, m, x):
        self.N = n  # 每层的高度
        self.M = m  # 楼盘的层数
        self.X = x  # 楼层号
        try:
            if self.M >= 100:
                raise MaxFloorException(self.M, 100)
            if self.X % 10 == 4 or self.X >= self.M:
                raise FloorNumException(self.X, self.M) 
        except MaxFloorException as result:
            print('MaxFloorException: 楼层总共有%d层, 要求不能大于等于100层.' % result.M)
            sys.exit()
        except FloorNumException as result:
            print('隔壁老王坐到第%d层， 要求带4的楼层不存在，并且要小于等于总楼层数：%d.' % (result.X, result.M))
            sys.exit()
    
    def __call__(self):
        '''
        output: 隔壁老王离地面的高度
        '''
        if self.X < 4:
            return self.N*(self.X - 1)
        else:
            return self.N*(self.X - 1 -((self.X - 4) // 10 + 1))

if __name__ == "__main__":
    print(Solution(3, 50, 1)())
    # print(Solution(3, 50, 4)())
    # print(Solution(3, 50, 27)())
    # print(Solution(3, 50, 51)())