class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        nums.sort()
        def backtrack(s,tracker) :
         res.append(tracker[:])
         if s == n :
            return 
         for i in range(s,n) :
            if i > s and nums[i] == nums[i-1] :
                continue
            temp = tracker[:]
            temp.append(nums[i])
            backtrack(i+1,temp)
        backtrack(0,[])
        return res




        





        # n = len(nums)
        # tracker = []
        # res = []
        # used = [False]*n
        # nums.sort()
        # def backtrack(s) :
        #     res.append(tracker[:])
        #     if s == n :
        #         return 
        #     for i in range(s,n) :
        #         if i > 0 and nums[i] == nums[i-1] and not used[i-1] : 
        #         ## the element before is equal horizontally to me and not vertically .. if vertically the used of him will be true      
        #             continue
        #         tracker.append(nums[i])
        #         used[i] = True
        #         backtrack(i+1)
        #         tracker.pop()
        #         used[i] = False
        # backtrack(0)
        # return res
        # n = len(nums)
        # tracker = []
        # res = []
        # nums.sort()
        # def backtrack(i) :
        #     if i == n :
        #         res.append(tracker[:])
        #         return 
            
        #     ## choose to include the element
        #     tracker.append(nums[i])
        #     backtrack(i+1)

        #     ## choose to not include the element 
        #     tracker.pop()
        #     while i+1 < n and nums[i] == nums[i+1] :
        #             i+=1
        #     backtrack(i+1)
        # backtrack(0)
        # return res
