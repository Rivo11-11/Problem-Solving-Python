class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_1 = 0
        maxx = 0
        for i in range(len(nums)) :
            if nums[i] == 1 :
                count_1 += 1
            else :
                maxx = max(maxx,count_1)
                count_1 = 0 
        return max(count_1,maxx)
         