'''
@Author: your name
@Date: 2020-06-19 11:24:17
@LastEditTime: 2020-06-19 16:22:35
@LastEditors: Please set LastEditors
@Description: 
给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。

示例:
给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

          0 
         / \ 
       -3   9 
       /   / 
    -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-height-tree-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
@FilePath: /leetcoding/tree-1.py
'''
# import math


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def sorted_array_to_bst(self, nums):
        if not len(nums):
            return
        # mid = math.ceil(len(nums)/2) -1     # 上入整数 floor(下入整数) 
        mid = len(nums)//2  # 如果长度是偶数就取右边的为根结点
        root = TreeNode(nums[mid])
        root.left = self.sorted_array_to_bst(nums[:mid])
        root.right = self.sorted_array_to_bst(nums[mid+1:])
        return root

if __name__ == '__main__':
    data = [-10,-3,0,5,9]
    s = Solution().sorted_array_to_bst(data)
    # 层序遍历(把每一层的node存储到sequence)
    if not s:
        print('None')
    else:
        seq = [s]
        res = [s.val]
        while seq:
            tmp = []
            for node in seq:
                if not node.left and not node.right:
                    break
                if node.left:
                    tmp.append(node.left)
                    res.append(node.left.val)
                else:
                    res.append(node.left)
                if node.right:
                    tmp.append(node.right)
                    res.append(node.right.val)
                else:
                    res.append(node.right)
                # res.append(node.val)
            seq = tmp
        print(res)