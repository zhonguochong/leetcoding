'''
@Author: your name
@Date: 2020-06-19 13:59:42
@LastEditTime: 2020-06-19 13:59:42
@LastEditors: Please set LastEditors
@Description:
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
@FilePath: /leetcoding/tree-2.py
'''
class TreeNode(object):
    def __init__(self, x)
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def max_depth(self, root):
        # ====================
        #    BFS(队列)（层序遍历）
        # ====================
        if not root:
            return 0
        seq = [root]
        res = 0
        while seq:
            tmp = []
            for node in seq:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            seq = tmp
            res += 1
        return res
        # =====================
        #     DFS(递归)（后序遍历）
        # =====================
        if not root:
            return 0
        else:
            return max(self.max_depth(root.left), self.max_depth(root.right)) + 1

if __name__ == "__main__":
    s = Solution()
    s.max_depth()        