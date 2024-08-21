class Solution(object):
    def arrayPairSum(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """
        # maxi = nums[0] 
        # mini = nums[0]
        # res = []
        # mymap = defaultdict(int)
        # n = len(nums)
        # ## count frequencies
        # for i in range(n) :
        #     maxi = max(maxi,nums[i]) 
        #     mini = min(mini,nums[i])
        #     mymap[nums[i]] += 1

        # for i in range(mini , maxi + 1) :
        #     if i in mymap : 
        #         res.extend([i]*mymap[i]) 
        res = sorted(nums)
        i = 1
        s = 0
        for num in res :
            ## if odd
            if i % 2 :
                s += num 
            i+=1
        return s


