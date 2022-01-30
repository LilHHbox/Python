#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sec=[]
        if not root:
            return False
        node=root
        res=0
        while len(sec) > 0 or node != None:
            while node != None:#迭代法：相当于显式的构造一个栈
                sec.append(node)
                res+=node.val
                node = node.left
            if res==targetSum:
                return True
            node = sec.pop()
            if not node.left and not node.right:
               res-=node.val
            node = node.right
        return False
# @lc code=end

