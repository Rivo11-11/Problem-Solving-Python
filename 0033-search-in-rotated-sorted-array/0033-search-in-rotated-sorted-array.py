class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0,len(nums) - 1
        while l <= r :
            mid = l + (r-l) // 2 
            if nums[mid] == target :
                return mid

            ## Fetch left if it is related to the left
            elif nums[mid] >= nums[l] :
                if  nums[l] <= target < nums[mid] :
                    r = mid - 1
                else :
                    l = mid + 1
            ## Fetch right
            else :
                if nums[mid] < target <= nums[r] :
                    l = mid + 1
                else :
                    r = mid - 1
        return -1
        