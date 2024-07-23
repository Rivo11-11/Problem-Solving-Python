class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ##1)
        # count = Counter(nums)
        # ## sort based on count frequency then if the frequency is the same take the largest one to be first
        # nums.sort(key = lambda x : (count[x],-x))
        # return nums


        ##2) bucket sort optimized
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        count = Counter(nums)
        for num in nums:
            buckets[count[num]].append(num)
        result = []
        for bucket in buckets:
            if bucket:
                result.extend(sorted(bucket, reverse=True))
        return result

        