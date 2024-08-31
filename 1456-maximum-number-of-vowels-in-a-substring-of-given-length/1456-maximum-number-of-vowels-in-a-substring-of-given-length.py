class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        myset = {
            'a' ,
            'e' ,
            'i' ,
            'u' , 
            'o' ,
         }
        n = len(s)
        l,r = 0 ,0
        count_vowel = 0
        maxi = 0
        while r < n :
            if s[r] in myset :
                    count_vowel += 1
            if r-l+1 > k :
                if s[l] in myset :
                    count_vowel -= 1
                l+=1
            maxi = max(maxi,count_vowel)
            r+=1
        return maxi