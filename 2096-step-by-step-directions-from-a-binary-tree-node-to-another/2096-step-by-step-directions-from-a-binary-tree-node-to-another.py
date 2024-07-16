# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        def trav(root,s,value,length) :
            l = ''
            r = ''
            if root :
                if root.val == value :
                    return s[:] , length
                s.append('L')
                l = trav(root.left,s,value,length + 1)
                s.pop()
                if l :
                    return l
                s.append('R')
                r = trav(root.right,s,value,length + 1)
                s.pop()
                if r :
                    return r
                
        root_s,n1 = trav(root,[],startValue,0)
        root_t,n2 = trav(root,[],destValue,0)

        if not n1  : 
           return ''.join(root_t)
        l = 0
        while l < n1 and l < n2 :
                if root_s[l] == root_t[l] :
                    l+=1
                else : break
        return (n1-l) * 'U' + ''.join(root_t[l:])


             
                

        