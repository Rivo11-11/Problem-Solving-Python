# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root :
            return []
        queue = deque() 
        queue.append(root) 
        res = []
        while queue :
            maxi = float('-inf')
            for i in range(len(queue)) :
                node = queue.popleft()
                maxi = max(maxi,node.val)
                if node.left :
                    queue.append(node.left)
                
                if node.right :
                    queue.append(node.right) 
                
            
            res.append(maxi) 

        return res

                
                



        return []