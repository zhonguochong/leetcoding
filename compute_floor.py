'''
@Author: your name
@Date: 2020-06-23 11:23:48
@LastEditTime: 2020-06-23 13:59:51
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
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