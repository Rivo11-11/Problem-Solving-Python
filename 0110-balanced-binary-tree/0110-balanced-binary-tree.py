# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root,flag) :
            if not root :
                return (0,True) 
            l,r = dfs(root.left,flag),dfs(root.right,flag)
            if abs(l[0]-r[0]) <= 1 and l[1] and r[1] :
                return (max(l[0],r[0])+1,True) 
            else :
                return (max(l[0],r[0])+1,False)
        return dfs(root,True)[1]

            