class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mymap = defaultdict(int)
        prefix_sum = 0 
        mymap[prefix_sum] = 1
        count = 0 
        for num in nums :
            prefix_sum += num 
            if prefix_sum - k in mymap :
                count += mymap[prefix_sum-k]
            mymap[prefix_sum] += 1
        return count
            