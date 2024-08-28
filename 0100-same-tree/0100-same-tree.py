# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.flag = True
        def dfs(p,q) :
            if (p and not q) or (q and not p) :
                self.flag = False 
                return 
            if p and q :
                if  p.val != q.val :
                    self.flag = False
                    return 
                dfs(p.left,q.left) 
                dfs(p.right,q.right)
        dfs(p,q)
        return self.flag
