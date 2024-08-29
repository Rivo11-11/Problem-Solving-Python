class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) 
        res = 0 
        for i in range(n) :
            res ^= nums[i]
        return res