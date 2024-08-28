# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0 
        def dfs(root) :
            if not root :
                return 0 
            l,r = dfs(root.left) , dfs(root.right) 
            self.res = max(self.res,l+r)
            return max(l,r) + 1
        dfs(root)
        return self.res




        # res = [float('-inf')]

        # ## o(n^2)
        # def findDiameter(root) :
        #     if root :
        #         k = 0
        #         if root.left :
        #             k += 1
        #         if root.right :
        #             k   +=1
        #         temp = height(root.left,0) + height(root.right,0)+ k
        #         res[0] = max(res[0],temp)
        #         findDiameter(root.left)
        #         findDiameter(root.right)
        
        # ## o(n)
        # ## top down 
        # def height(root,count) :
        #     if not root :
        #         return count
        #     return  max(height(root.left,count+1),height(root.right,count+1))
        
        # ## bottom up
        # def height2(root) :
        #     if not root : 
        #         return 0 
        #     left = height2(root.left)
        #     right = height2(root.right) 
        #     return max(left,right) + 1

        # findDiameter(root)
        # print(height(root,0)) 
        # print(height2(root))
        # return res[0]

       
