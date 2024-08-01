# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root : return []
        queue = deque()
        queue.append(root)
        stack = []
        while queue :
            n = len(queue)
            temp = []
            for i in range(n) :
                node = queue.popleft()
                temp.append(node.val)
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
            stack.append(temp[:])
        result = []
        while stack :
            result.append(stack.pop())
        return result
