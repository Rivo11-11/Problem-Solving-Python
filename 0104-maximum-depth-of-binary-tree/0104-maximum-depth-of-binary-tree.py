# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def FindMaxD(root,count) :
            if not root :
                return 0
            if not (root.right or root.left) :
                return 1
            count =1
            count += max(FindMaxD(root.left,count ),FindMaxD(root.right,count ))
            return count
        return FindMaxD(root,0)