class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        c = 0 
        for i in range(n-1) :
            if nums[i] >= nums[i+1] :
                c += nums[i] - nums[i+1] + 1 
                nums[i+1] = nums[i] + 1 
        return c

        