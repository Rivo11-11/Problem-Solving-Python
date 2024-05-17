class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        change = s[0]
        count = 0
        for c in s :
            if change != c :
                change = c 
                res.append(count)
                count = 0
            count += 1
        res.append(count)
        ans = 0
        for i in range(len(res)-1) :
            ans += min(res[i],res[i+1])
        return ans
