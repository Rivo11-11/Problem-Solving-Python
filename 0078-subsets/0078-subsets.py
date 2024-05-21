class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## o(n*2^n)
        # n = len(nums)
        # res = []
        # tracker = []
        # def backtrack(s) :
        #     res.append(tracker[:])
        #     if s == n :
        #         return
        #     for i in range(s,n) :
        #         tracker.append(nums[i])
        #         backtrack(i+1)
        #         tracker.pop()
        # backtrack(0)
        # return res

        n = len(nums)
        tracker = []
        res = []
        def backtrack(i) :
            if i == n :
                print(tracker)
                res.append(tracker[:])
                return 
            
            ## choose to include the element
            tracker.append(nums[i])
            backtrack(i+1)

            ## choose to not include the element 
            tracker.pop()
            backtrack(i+1)
        backtrack(0)
        return res





