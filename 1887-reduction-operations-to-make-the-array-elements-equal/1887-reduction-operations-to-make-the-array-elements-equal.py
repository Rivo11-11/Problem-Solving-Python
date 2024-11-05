class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        ans = 0
        n = len(nums)
        for i in range(1,n) :
            if nums[i] == nums[i-1] :
                ans += count 
            else :
                count += 1
                ans += count
        return ans



            

        