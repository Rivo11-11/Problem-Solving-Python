# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def getSucc(root) :
            curr = root.right 
            while curr and curr.left :
                curr = curr.left
            return curr
        def delNode(root,key) :
                if not root  :
                    return root
                if root.val > key : 
                    root.left = delNode(root.left,key)
                elif root.val < key : 
                    root.right = delNode(root.right,key) 
                
                else : 
                    ## single child case
                    if not root.left :
                        return root.right
                    if not root.right :
                        return root.left
                    
                    ## 2 child case find the inorder successor
                    succ = getSucc(root) 
                    root.val = succ.val
                    ## turn the problem to delete this successor with that key ... 
                    root.right = delNode(root.right,succ.val)
                return root
        return delNode(root,key)

