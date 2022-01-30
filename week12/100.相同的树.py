#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        se1=[]
        se2=[]
        res1=[]
        res2=[]
        node1,node2=p,q
        while len(se1)>0 or node1!=None:
            while node1!=None:
                se1.append(node1)
                node1=node1.left
            if node1==None:
               res1.append('none')
            node1=se1.pop()
            res1.append(node1.val)
            node1=node1.right
        while len(se2)>0 or node2!=None:
            while node2!=None:
                se2.append(node2)
                node2=node2.left
            if node1==None:    
               res2.append('none')
            node2=se2.pop()
            res2.append(node2.val)
            node2=node2.right
            
            
        if res1==res2:
            return True
        return False

# @lc code=end

