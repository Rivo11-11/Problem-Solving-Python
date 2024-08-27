class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) 
        l,r = 0,n-1
        mini = float('inf')
        while l <= r : 
            mid = (l + r) // 2 
            if nums[mid] == nums[l] == nums[r]:
                mini = min(mini,nums[mid])
                l+=1
                r-=1
            elif nums[l] <= nums[mid] :
                mini = min(nums[l],mini) 
                l = mid + 1 
            else :
                mini = min(nums[mid],mini)
                r = mid - 1    
        return mini        