# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ## return the height of the tree o(h)
        def count(root) :
            ## o(lgn)
            def find(root) :
                if not root :
                    return 0
                return 1 + find(root.left) 
            
            if not root :
                return 0
            if not root.left and not root.right  :
                return 1
            leftheight = find(root.left)
            rightheight = find(root.right)
            
            ## then for sure the leftsubtree is perfect all nodes filled
            if leftheight == rightheight :
                return 2**leftheight + count(root.right)
            else :
                return 2**rightheight + count(root.left) 
        


        return count(root)

        