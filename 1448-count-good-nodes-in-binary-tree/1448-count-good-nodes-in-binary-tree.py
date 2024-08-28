# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(root,maxi) : 
            if not root :
                return 
            if root.val >= maxi :
                self.res += 1
                maxi = root.val
            dfs(root.left,maxi)
            dfs(root.right,maxi)
        dfs(root,root.val)
        return self.res
        