class Solution(object):
    def countBeautifulPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        count = 0
        n = len(nums)
        for i in range(n) :
            val1 = int(str(nums[i])[0])
            for j in range(i+1,n) :
               val2 = int(str(nums[j])[-1])
               if gcd(val1,val2) == 1 :
                 count += 1
        return count

        