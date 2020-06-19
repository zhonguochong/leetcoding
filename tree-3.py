'''
@Author: your name
@Date: 2020-06-19 16:55:46
@LastEditTime: 2020-06-19 17:04:18
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

 

示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
@FilePath: /leetcoding/tree-3.py
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def jinxiang(self, root):
        if not root:
            return
        else:
            seq = [root]
            while seq:
                for node in seq:
                    tmp = []
                    node.left, node.right = node.right, node.left
                    tmp.append(node.left)
                    tmp.append(node.right)
                seq = tmp
        return root