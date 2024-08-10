# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque() 
        queue.append(root)
        sum = 0
        while queue : 
            n = len(queue)
            sum = 0
            for i in range(n) :
                node = queue.popleft() 
                sum += node.val
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
        return sum
                
        