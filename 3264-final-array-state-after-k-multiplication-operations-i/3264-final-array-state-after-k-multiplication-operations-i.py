class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        n = len(nums)
        heap = []
        for i in range(n) :
            heapq.heappush(heap,(nums[i],i))

        for i in range(k) :
                    _ , index = heapq.heappop(heap)
                    nums[index] *= multiplier
                    heapq.heappush(heap,(nums[index],index)) 
        return nums
        