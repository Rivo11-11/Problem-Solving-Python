class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        ## brute force o(n^2)
        # n = len(nums)
        # mini = float("inf")
        # for i in range(n):
        #     temp = nums[i]
        #     if temp >= target :
        #         return 1
        #     for j in range(i+1,n) :
        #         temp += nums[j]
        #         if temp >= target :
        #             mini = min(mini,j - i + 1)
        #             break 
        # if mini == float("inf") :
        #     return 0
        # return mini

        ## o(n) solution
        f,l = 0,0 
        n = len(nums)
        temp = 0
        mini = float("inf")
        while l < n :
            temp += nums[l]
            if temp >= target :
                mini = min(mini,l-f+1)
                temp -= nums[f]
                temp -= nums[l]
                f+=1
                continue
            l+=1
        if mini == float("inf") :
            return 0
        return mini






        