class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## 1 use a sorted array 

        # temp = sorted(nums)
        # n = len(nums)
        # l,r = 0,n-1
        # while l < n and nums[l] == temp[l] : l+=1
        # while r > l and nums[r] == temp[r] : r-=1
        # return r-l+1


        ## 2 o(n) time . o(1) space solution 
        start = -1 
        end = -1
        maxi = float('-inf')
        mini = float('inf')
        n = len(nums)
        for i in range(n) : ## left to right
            if nums[i] >= maxi :
                maxi = nums[i]
            else :
                end = i       
        for i in range(n-1,-1,-1) : ## right to left
            if nums[i] <= mini :
                mini = nums[i]
            else :
                start = i 
        if start == end == -1 : return 0 
        return end - start + 1    




        