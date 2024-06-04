class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mymap = {
            'I'  : 1 ,          
            'V'  :  5,
            'X'  : 10,
            'L'  : 50,
            'C'  : 100,
            'D'  : 500,
            'M'  :1000
        }
        n = len(s)
        res = 0
        i = 0
        while i < n : 
            if i+1 < n and mymap[s[i]] < mymap[s[i+1]] :
                res += mymap[s[i+1]] - mymap[s[i]] 
                i+=2
            else :
                res += mymap[s[i]]
                i+=1
        return res

 
        