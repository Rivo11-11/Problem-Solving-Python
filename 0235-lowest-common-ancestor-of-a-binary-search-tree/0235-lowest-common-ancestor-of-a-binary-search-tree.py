# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.maxi = max(p.val,q.val) 
        self.mini = min(p.val,q.val)
        def dfs(root) :
            if root :
                if  self.mini <= root.val <= self.maxi :
                    return root 
                elif root.val > self.maxi : 
                    return dfs(root.left) 
                else :
                    return dfs(root.right)
        return dfs(root)
                