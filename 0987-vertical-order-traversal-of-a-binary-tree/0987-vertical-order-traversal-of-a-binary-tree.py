# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        mymap = {}
        def dfs(root,row,col) :
            if root :
                if col not in mymap :
                    mymap[col] = [(root.val,row)]
                else :
                   mymap[col].append((root.val,row))
                   mymap[col].sort(key = lambda x : (x[1],x[0]) )
                dfs(root.left,row+1,col-1) 
                dfs(root.right,row+1,col+1)
        dfs(root,0,0)
        keys = mymap.keys() 
        keys.sort() 
        result = []
        for key in keys :
            res = []
            for tup in mymap[key] :
                res.append(tup[0])
            result.append(res[:])
        return result

      
            
            
    
        