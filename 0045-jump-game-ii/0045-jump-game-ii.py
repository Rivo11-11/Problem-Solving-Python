class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # mini = [float('inf')]
        # mymap = {}
        # def backtrack(position,count) :
        #     if position == n-1 :
        #         mini[0] = min(mini[0],count)
        #         return 
        #     if position > n-1 :
        #         return 
        #     if position in mymap :
        #         mini[0] = min(mini[0],count + mymap[position])
        #         return 
        #     ## find the best nums[position]
        #     local_min = float('inf')
        #     for i in range(1, nums[position] + 1):
        #         backtrack(position + i, count + 1)
        #         local_min = min(local_min, mini[0] - count)
        #     mymap[position] = local_min
        # backtrack(0,0)
        # return mini[0]
        n = len(nums) 
        l = r = 0
        res = 0
        while r < n-1 :
            max_jump = float('-inf')
            for i in range(l,r+1) :
                max_jump = max(max_jump,nums[i] + i) 
            l = r+1 
            r = max_jump 
            res += 1
        return res



        