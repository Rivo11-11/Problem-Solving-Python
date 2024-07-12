class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [1,2,3,4,5,6,7,8,9]
        res = []
        def backtrack(s,tracker,l,tot) :
            if tot == n and l == k :
                res.append(tracker[:])
                return 
            if s == 9 or l > k or tot > n :
                return
            for i in range(s,9) :
                temp = tracker[:]
                temp.append(nums[i])
                backtrack(i+1,temp,l+1,tot + nums[i])
        backtrack(0,[],0,0)
        return res










        # tracker = []
        # res = []
        # candidates = [1,2,3,4,5,6,7,8,9]
        
        # def backtrack(i,sum) :
        #     if sum == n and len(tracker) == k :
        #         res.append(tracker[:])
        #         return 
        #     if sum > n or i == 9 :
        #         return 

        #     ## take the element
        #     tracker.append(candidates[i])
        #     sum += candidates[i]
        #     backtrack(i+1,sum)

        #     ## pop and take another direction but consider the duplication
        #     tracker.pop()
        #     sum -= candidates[i]
        #     backtrack(i+1,sum)
        # backtrack(0,0)
        # return res
        