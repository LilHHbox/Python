#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        def mindepth(root):
            if root is None: 
                return 0 
            elif not root.left and not root.right:
                return 1
            elif  not root.left:
                return mindepth(root.right)+1
            elif not root.right:
                return mindepth(root.left)+1
            else:   
                left_height = mindepth(root.left) 
                right_height = mindepth(root.right) 
                return min(left_height, right_height)+1
        return  mindepth(root)



# @lc code=end

