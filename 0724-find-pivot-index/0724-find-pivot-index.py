class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix_sum = [0 for i in range(n)]
        suffix_sum = [0 for i in range(n)]
        j = n-1
        prefix_sum[0] = nums[0]
        suffix_sum[n-1] = nums[n-1]
        for i in range(1,n) :
            prefix_sum[i] += nums[i] + prefix_sum[i-1]
            suffix_sum[n-1-i] += nums[n-1-i] + suffix_sum[j]
            j-=1 
        for i in range(0,n) :
            ## to get the the left most pivot start from the left and compare with the suffix
            if prefix_sum[i] == suffix_sum[i] :
                return i

        return -1

        