# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root,lower,greater) :

            if not root :
                return True
            if root.val > lower and root.val < greater :
                return dfs(root.left,lower,root.val) and dfs(root.right,root.val,greater)

            else :
                return  False

        return dfs(root,float("-inf"),float("inf"))
    
        

        