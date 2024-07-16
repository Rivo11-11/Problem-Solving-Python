class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0, 0
        n = len(nums)
        maxi = 0
        current_sum = 0
        mymap = defaultdict(int)
        length = 0 
        while r < n:
            current_sum += nums[r]
            mymap[nums[r]] += 1
            length += 1
            
            if length > k:
                mymap[nums[l]] -= 1 
                if mymap[nums[l]] == 0 :
                     del mymap[nums[l]]
                current_sum -= nums[l]
                length -= 1
                l += 1
            if length == k == len(mymap):
                maxi = max(maxi, current_sum)
            r += 1

        return maxi








