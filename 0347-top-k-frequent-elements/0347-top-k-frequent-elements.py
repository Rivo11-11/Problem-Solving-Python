class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums) 
        number  = max(count.values())
        buckets = [[] for i in range(number)]
        for num in set(nums) :
            buckets[count[num] -1 ].append(num)
        res = []
        for bucket in reversed(buckets) :
            if k == 0 :
                break
            res.extend(bucket)
            k-= len(bucket)
        return res