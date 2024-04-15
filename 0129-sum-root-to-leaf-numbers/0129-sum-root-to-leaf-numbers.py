# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        res.append(0)
        def dfs(root,temp) :
            if not root : return 
            if not root.left and not root.right : 
                temp += str(root.val)
                res[0] += int(temp)
                return
            dfs(root.left, temp + str(root.val)) 
            dfs(root.right,temp + str(root.val)) 
            
        dfs(root,"")
        return res[0]