class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 4 :
            return 0
        nums.sort()
        val1 = nums[n-4] - nums[0]
        val2 = nums[n-3] - nums[1] 
        val3 = nums[n-2] - nums[2]
        val4 = nums[n-1] - nums[3]
        return min(val1,val2,val3,val4)
       
            
        