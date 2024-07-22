class Solution(object):
    def getSubarrayBeauty(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l,r =0,0
        n = len(nums)
        count_map = defaultdict(int)
        res = []
        while r < n:
            count_map[nums[r]] += 1
            if r - l + 1 == k:
                neg_count = 0
                beauty = 0
                for num in range(-50, 0):
                    neg_count += count_map[num]
                    if neg_count >= x:
                        beauty = num
                        break
                res.append(beauty)
                count_map[nums[l]] -= 1
                l += 1
            r+= 1

        return res

       