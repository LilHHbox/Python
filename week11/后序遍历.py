# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        stack, node = [root], root
        resLs = []
        while stack.__len__() > 0:
            node = stack.pop()
            resLs.append(node.val)
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)
        return [val for val in reversed(resLs)]


#通过层次遍历每次先打印右节点，然后再使用一次倒序打印所有的结果
