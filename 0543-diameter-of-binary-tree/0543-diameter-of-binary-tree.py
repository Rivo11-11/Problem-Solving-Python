# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ## DFS 
        ## 1 Brute Force o(n^2)
        if not root  or not (root.left or root.right):
            return 0
        diameter = 0
        def findDiameter(root,count) :
            if not root :
                return 0
            if  not (root.left or root.right) :
                return 1
            count = 1
            count += max(findDiameter(root.left,count),findDiameter(root.right,count))  
            return count
        queue = deque()
        queue.append(root)
        max_root = float("-inf")
        while queue :
            print(len(queue))
            for i in range(len(queue)) :
                node = queue.popleft()
                if node :
                    max_root = max(max_root,findDiameter(node.left,diameter) +  findDiameter(node.right,diameter))
                    queue.append(node.left)
                    queue.append(node.right)

        return max_root

        ## Optimized o(n)
        

        


        