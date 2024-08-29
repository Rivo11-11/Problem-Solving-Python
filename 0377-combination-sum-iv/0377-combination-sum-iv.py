class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ## 1) backtracking
        # n = len(nums)
        # self.res = 0
        # def backtrack(tot):
        #     if tot == target :
        #         self.res += 1 
        #         return 
        #     if tot > target :
        #         return 
        #     for i in range(n) :
        #         backtrack(tot+nums[i])
        # backtrack(0)
        # return self.res

        ## 2) Dynamic programming 
        dp = {
            0 : 1 
        }
        nums.sort()
        for i in range(1,target+1) :
            dp[i] = 0 
            for num in nums :
                if i-num < 0 :
                    break
                dp[i] += dp[i-num]
        
        return dp[target]
            












        




        