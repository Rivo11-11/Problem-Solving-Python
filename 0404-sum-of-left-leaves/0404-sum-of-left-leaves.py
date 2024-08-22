# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = [0]
        def dfs(root,flag) :
            if root :
                dfs(root.left,True) 
                dfs(root.right,False)
                ## if it is a leaf node and has the flag = True a left leaf
                if not root.left and not root.right and flag :
                    s[0] += root.val
        dfs(root,False)
        return s[0]

        