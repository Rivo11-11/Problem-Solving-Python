class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        flag = [False] * n
        def backtrack(tracker,l) : 
            if l == n :
                res.append(tracker[:])
                return 
            for i in range(n) :
                if flag[i] == False :
                    temp = tracker[:]
                    temp.append(nums[i])
                    flag[i] = True
                    backtrack(temp,l+1) 
                    flag[i] = False

        backtrack([],0)
        return res