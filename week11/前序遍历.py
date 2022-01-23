

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:  # 方法1
        if not root:
            return []
        se = []
        res = []
        node = root
        while len(se) > 0 or node != None:
            while node != None:  # 迭代法：相当于显式的构造一个栈
               res.append((node.val))
               se.append(node)
               node=node.left
            node=se.pop()
            node=node.right
        return res