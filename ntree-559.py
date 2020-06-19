'''
@Author: your name
@Date: 2020-06-09 11:33:33
@LastEditTime: 2020-06-09 11:37:35
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /studyleetcode/ntree-559.py
'''
class Node():
    def __init__(self, val, children):
        self.val = val
        self.children = children
class Solution():
    def max_depth(self, root):
        if root is None:
            return 0
        elif root.children == []:
            return 1
        else:
            height = [self.max_depth(c) for c in root.children]
            return max(height) + 1

grah  = [1, None, 3, 2, 4, None, 5, 6]
grah_node = Node(grah)
s = Solution().max_depth(grah_node)
print(s)