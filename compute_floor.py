class MaxFloorException(Exception):
    def __init__(self, m):
        self.M = m
class FloorNumException(Exception):
    def __init__(self, x):
        self.X = x
class Solution(object):
    def __init__(self, n, m, x):
        self.N = n  # 每层的高度
        self.M = m  # 楼盘的层数
        self.X = x  # 楼层号
        try:
            if self.M >= 100:
                raise MaxFloorException(self.M, 100)
            if self.X % 10 == 4 and self.X <= self.M:
                raise FloorNumException(self.X, self.M) 
        except MaxFloorException as result:
            print('MaxFloorException: input floors is %d, not greater than 100.' % result.M)
        except FloorNumException as result:
            print('input floor number: %d cannot have 4 and smller than %d.' % (self.X, self.M))
    def __call__(self):
        '''
        output: 隔壁老王离地面的高度
        '''
        if self.X < 4:
            return self.N(self.X-1)
        elif x