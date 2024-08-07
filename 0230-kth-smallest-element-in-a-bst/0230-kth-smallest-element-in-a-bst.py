# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        def Inorder(root) :
            if root :
                Inorder(root.left) 
                res.append(root.val)
                Inorder(root.right)
        Inorder(root) 
        return res[k-1]
            
        