

#显然中序遍历输出结果相等但树不一定相等
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        se1 = []
        se2 = []
        res1 = []
        res2 = []
        node1, node2 = p, q
        while len(se1) > 0 or node1 != None:
            while node1 != None:
                se1.append(node1)
                node1 = node1.left
            if node1 == None:
                res1.append('none')
            node1 = se1.pop()
            res1.append(node1.val)
            node1 = node1.right
        while len(se2) > 0 or node2 != None:
            while node2 != None:
                se2.append(node2)
                node2 = node2.left
            if node1 == None:
                res2.append('none')
            node2 = se2.pop()
            res2.append(node2.val)
            node2 = node2.right

        if res1 == res2:
            return True
        return False


#深度优先：
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#广度优先
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val != node2.val:
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if (not left1) ^ (not left2):
                return False
            if (not right1) ^ (not right2):
                return False
            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)

        return not queue1 and not queue2


