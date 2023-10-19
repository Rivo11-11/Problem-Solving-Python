class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        start = 0
        end = n - 1
        while start <= end :
            if nums[end] == val :
                nums[end] = "_"
                end -=1 
                continue
            if nums[start] == val :
                nums[start] = nums[end]
                nums[end] = "_"
                end -=1
            start +=1
        return end  + 1
        