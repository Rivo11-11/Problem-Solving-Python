class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l , r  = 0 , len(nums) - 1
        result = float("inf")
        while l <= r :
            mid = l + (r-l) // 2
            ## related to the left sorted  ?
            if nums[mid] >= nums[l] :
                result = min(result,nums[l]) 
                l = mid + 1
            ## related to the right sorted ?
            else :
                result = min(result,nums[mid]) 
                r = mid - 1
        return result



        