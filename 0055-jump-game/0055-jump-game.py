class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        goal = n-1 
        for i in range(n-1,-1,-1) :
            if nums[i] + i >= goal :
                goal = i 
        if goal == 0 :
            return True 
        return False
        