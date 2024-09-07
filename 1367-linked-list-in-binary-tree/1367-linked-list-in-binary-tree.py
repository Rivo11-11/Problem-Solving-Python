# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(head,root) :
            
            if root and head :
                if head.val == root.val :
                    
                    ## this is the last value of the list
                    if head.next == None :
                        return True
                    return dfs(head.next,root.left) or dfs(head.next,root.right) 
                else :
                    return False
        def helper(root) :
            if root :
                flag = dfs(head,root)
                if flag :
                    return True
                return helper(root.left) or helper(root.right)
            

        return helper(root)
            
        
        