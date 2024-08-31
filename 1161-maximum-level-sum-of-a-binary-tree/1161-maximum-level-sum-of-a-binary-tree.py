# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque()
        queue.append(root) 
        res = 0
        prevsum = float('-inf')
        level = 1
        while queue :
            sum = 0
            for i in range(len(queue)) :
                node = queue.popleft() 
                sum += node.val
                if node.left :
                    queue.append(node.left) 
                if node.right :
                    queue.append(node.right)
            if sum > prevsum :
                res = level 
                prevsum = sum
            level +=1
        return res