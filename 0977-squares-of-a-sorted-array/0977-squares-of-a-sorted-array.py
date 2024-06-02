class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        r = n - 1
        l = 0 
        res = [0]  *n
        i = n - 1
        while l <= r :
            if abs(nums[r]) > abs(nums[l]) :
                res[i] = nums[r] ** 2
                r-=1
                i-=1 
            else :
                res[i] = nums[l] ** 2 
                l += 1 
                i -= 1 
        return res