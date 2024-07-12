class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        nums.sort()
        flag = [False] * n
        def backtrack(tracker,l) :
            if l == n :
                res.append(tracker[:])
                return 
            for i in range(n) :
                if i > 0 and nums[i] == nums[i-1] and flag[i-1] == False :
                    continue 
                if flag[i] == False :
                    temp = tracker[:]
                    temp.append(nums[i])
                    flag[i] = True
                    backtrack(temp,l+1)
                    flag[i] = False
        backtrack([],0)
        return res

        