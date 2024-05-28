class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() 
        n = len(nums)
        count = -1 
        for i in range(n) :
            before = nums[i-1] if i-1 > -1 else float('-inf')
            if nums[i] == before :
                continue
            if nums[i] ==  n-i :
                return nums[i] 
            if  before < n-i < nums[i] :
                count = n-i
        return count