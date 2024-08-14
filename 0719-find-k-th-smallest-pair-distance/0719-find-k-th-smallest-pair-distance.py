class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()  
        n = len(nums) 
        def count(diff) :
            l = 0
            res = 0
            for r in range(n) :
                while nums[r] - nums[l] > diff :
                    l += 1
                res += r - l
            return res
                
        l,r = 0,max(nums) ## range of possible difference
        while l < r  :
            mid = (l+r) // 2 
            n_pairs = count(mid)

            ## answers in this range but i need to be more specific found the closet one
            if n_pairs >= k :
                r = mid 
            
            ## i am sure the left_part is not with me i need to throw it
            else :
                l = mid + 1
        return r

        
        