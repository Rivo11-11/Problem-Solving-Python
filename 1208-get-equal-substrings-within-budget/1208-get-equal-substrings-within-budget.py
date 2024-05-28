class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        max_length = 0
        l = 0
        cost = 0
        for r in range(len(s)) :
            cost += abs(ord(s[r]) - ord(t[r]))
            while cost > maxCost :
                cost -= abs(ord(s[l]) - ord(t[l]))
                l+=1
            max_length = max(max_length,r-l+1)
            r+=1
        return max_length


        