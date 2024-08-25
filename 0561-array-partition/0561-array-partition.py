class Solution(object):
    def arrayPairSum(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() 
        n = len(nums)
        s = 0
        for i in range(n) :
            if i % 2 == 0: 
                s += nums[i]
        return s



