class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count_1 = 0 
        for num in nums :
            if num == 1 : count_1 += 1

        ## search for max window of size ##1 that contains the most 1 
        l,r = 0,0 
        maxi = 0
        temp_1 = 0
        while r < 2*n :
            if nums[r%n] == 1 :
                temp_1 += 1
            if r-l+1 == count_1 :
                maxi = max(maxi,temp_1)
                if nums[l%n] == 1 :
                    temp_1 -= 1
                l+=1
            r += 1
        return count_1 - maxi




        