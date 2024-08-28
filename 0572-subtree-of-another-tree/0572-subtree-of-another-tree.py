# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def isSame(root,subroot) :
            if not root and not subroot :
                return True
            if (root and not subroot) or (subroot and not root) :
                return False
            if root.val == subroot.val and isSame(root.left,subroot.left) and isSame(root.right,subroot.right) :
                return True
        def traverse(root,subroot) :
            if not root :
                return False
            if isSame(root,subroot) :
                return True 
            return traverse(root.left,subroot) or traverse(root.right,subroot)
        return traverse(root,subRoot)

        