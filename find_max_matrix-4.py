'''
@Author: your name
@Date: 2020-06-24 10:02:40
@LastEditTime: 2020-06-24 11:10:15
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
4. 给定一 M 乘 N 的 0,1 矩阵，找到其中最大的以 1 为边的矩形。（不考虑斜 45°情况）
@FilePath: /leetcoding/find_min_matrix.py
'''
class Solution:
    def max_1_bordered_matrix(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        max_len = 0
        m, n = len(grid), len(grid[0])
        # 遍历每个点
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    flag1 = True
                    curr_len = max_len
                    while i + curr_len < m and j + curr_len < n:
                        flag2 = True
                        # 如果‘左边界‘有0， 那么检查下一个点
                        for a in range(i, i + curr_len + 1):
                            if grid[a][j] != 1:
                                flag1 = False
                                break
                        if not flag1:
                            break
                        # 如果‘上边界‘有0， 那么检查下一个点
                        for b in range(j, j + curr_len + 1):
                            if grid[i][b] != 1:
                                flag1 = False
                                break
                        if not flag1:
                            break
                        # 如果’右边界’有0， 那么继续在这一点，检查边长+1的矩形
                        for a in range(i, i + curr_len + 1):
                            if grid[a][j + curr_len] != 1:
                                curr_len += 1
                                flag2 = False
                                break
                        if not flag2:
                            continue
                        # 如果’下边界’有0， 那么继续在这一点，检查边长+1的矩形
                        for b in range(j, j + curr_len + 1):
                            if grid[i + curr_len][b] != 1:
                                curr_len += 1
                                flag2 = False
                                break
                        if not flag2:
                            continue
                        curr_len += 1
                        max_len = curr_len
        return max_len


if __name__ == '__main__':
    s = Solution()
    print('最大矩形的边长为：%d' % s.max_1_bordered_matrix([[1,1,1],[1,0,1],[1,1,1]]))
    # print('最大矩形的边长为：%d' % s.max_1_bordered_matrix([[1,1],[0,1],[1,1]]))
    # print('最大矩形的边长为：%d' % s.max_1_bordered_matrix([[1,1,1,1],[1,0,0,1],[1,1,1,1]]))