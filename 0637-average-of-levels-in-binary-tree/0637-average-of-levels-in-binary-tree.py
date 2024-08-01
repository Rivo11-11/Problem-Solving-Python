# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ## BFS search
        queue = deque()
        queue.append(root)
        result = []
        while queue :
            n = len(queue)
            s = 0
            for i in range(n) :
                node = queue.popleft()
                s += node.val
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
            result.append(1.0*s/n)
        return result
                
        