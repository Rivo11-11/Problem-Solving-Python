# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        myset = set(to_delete) 
        res  = []
        def dfs(root,flag) :
            if root :
                if root.val in myset :
                    root.left = dfs(root.left,True)
                    root.right = dfs(root.right,True)
                    return None
                else  :
                    if flag :
                     res.append(root)
                    root.left = dfs(root.left,False)
                    root.right = dfs(root.right,False)
            return root
           

        dfs(root,True)
        return res