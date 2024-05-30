class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count_0 = 0 
        maxx = 0 
        l = 0 
        for r in range(len(nums)) :
            if nums[r] == 0 :
                count_0 += 1
            while k < count_0 :
                if nums[l] == 0 : 
                    count_0 -= 1
                l+=1
            maxx = max(maxx,r-l+1)
        return maxx
        