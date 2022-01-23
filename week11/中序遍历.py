# Author: Lilbox
# Time:2022/1/22 10:33

class TreeNode:


def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:#方法1
        if not root:
            return []
        se = []
        res = []
        node = root
        while len(se) > 0 or node != None:
            while node != None:#迭代法：相当于显式的构造一个栈
                se.append(node)
                node = node.left
            node = se.pop()
            res.append(node.val)
            node = node.right
        return res
    def inorderTraversal1(self, root: TreeNode) -> List[int]:#方法2
        res = []
        def inorder(root):
            if not root:#递归法
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res

