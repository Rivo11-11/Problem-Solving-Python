# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        # def dfs(root) :
        #     if not root :
        #         return True
        #     if not root.left and not root.right :
        #         if root.val == target :
        #             root.val = 0
        #             return True
        #         return
        #     val1 = dfs(root.left)
        #     val2 = dfs(root.right)
        #     if val1 and val2 :
        #             if root.val == target :
        #                 root.val = 0
        #                 return True
        # dfs(root)
        # def construct(root):
        #     if not root or root.val == 0:
        #         return None
        #     new_root = TreeNode(root.val)
        #     new_root.left = construct(root.left)
        #     new_root.right = construct(root.right)
        #     return new_root

        # return construct(root)
        def dfs(root):
            if not root:
                return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if not root.left and not root.right and root.val == target:
                return None
            return root
        return dfs(root)
    