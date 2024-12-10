class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        prefix = [1 for num in nums] 
        n = len(nums)
        for i in range(1,n) :
            if (nums[i] + nums[i-1]) % 2 :
                prefix[i] += prefix[i-1] 
 
        res = []
        for start,end in queries :
            if prefix[end] < end-start+1 :
                res.append(False)
            else :
                res.append(True)
        return res

        