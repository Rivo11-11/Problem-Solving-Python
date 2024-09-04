class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ## weird logic 
        f = float('inf')
        s = float('inf')
        n = len(nums)
        for i in range(n) :
            if nums[i] <= f :
                f = nums[i] 
            elif nums[i] <= s :
                s = nums[i] 
            else :
                return True 
        return False



