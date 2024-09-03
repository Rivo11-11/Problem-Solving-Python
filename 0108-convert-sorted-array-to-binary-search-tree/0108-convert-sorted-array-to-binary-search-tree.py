# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(nums[0])
        n = len(nums)
        l,r = 0,n-1
        root = None
        def InsertBst(l,r,root) :
            while l <= r :
                mid = (l+r) // 2
                root = TreeNode(nums[mid])
                root.left = InsertBst(l,mid-1,root.left)
                root.right = InsertBst(mid+1,r,root.right)
                return root
        return InsertBst(l,r,root)


        