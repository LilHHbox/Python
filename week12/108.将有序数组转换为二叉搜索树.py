#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, num: List[int]) -> TreeNode:
        
         def creatTree(left,right,nums):
                if left>right:
                    return None
                mid=(left+right)//2
                mid_node=TreeNode(nums[mid])
                mid_node.left=creatTree(left,mid-1,nums)
                mid_node.right=creatTree(mid+1,right,nums)
                return mid_node
         return creatTree(0,len(num)-1,num)
         
# @lc code=end

