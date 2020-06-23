'''
@Author: your name
@Date: 2020-06-23 15:14:40
@LastEditTime: 2020-06-23 15:47:11
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
4. 给定一 M 乘 N 的 0,1 矩阵，找到其中最大的以 1 为边的矩形。（不考虑斜 45°情况）
@FilePath: /leetcoding/find_min_matrix.py
'''
class Solution:
    def max_1_bordered_matrix(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        maxLen = 0
        m, n = len(grid), len(grid[0])
        # 遍历每个点
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    flag1 = True
                    currLen = maxLen
                    while i + currLen < m and j + currLen < n:
                        flag2 = True
                        # 如果‘左边界‘有0， 那么检查下一个点
                        for a in range(i, i + currLen + 1):
                            if grid[a][j] != 1:
                                flag1 = False
                                break
                        if not flag1:
                            break
                        # 如果‘上边界‘有0， 那么检查下一个点
                        for b in range(j, j + currLen + 1):
                            if grid[i][b] != 1:
                                flag1 = False
                                break
                        if not flag1:
                            break
                        # 如果’右边界’有0， 那么继续在这一点，检查边长+1的正方形
                        for a in range(i, i + currLen + 1):
                            if grid[a][j + currLen] != 1:
                                currLen += 1
                                flag2 = False
                                break
                        if not flag2:
                            continue
                        # 如果’下边界’有0， 那么继续在这一点，检查边长+1的正方形
                        for b in range(j, j + currLen + 1):
                            if grid[i + currLen][b] != 1:
                                currLen += 1
                                flag2 = False
                                break
                        if not flag2:
                            continue
                        currLen += 1
                        maxLen = currLen
        return maxLen


s = Solution()
print('最大矩形的边长为：%d' % s.max_1_bordered_matrix([[1,1,1],[1,0,1],[1,1,1]]))
# print('最大矩形的边长为：%d' % s.max_1_bordered_matrix([[1,1],[0,1],[1,1]]))
# print('最大矩形的边长为：%d' % s.max_1_bordered_matrix([[1,1,1,1],[1,0,0,1],[1,1,1,1]]))