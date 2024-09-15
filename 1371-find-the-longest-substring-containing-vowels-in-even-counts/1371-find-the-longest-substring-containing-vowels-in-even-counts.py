class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## a e i o u
        mymap = {
            'a' : 0 ,
            'e' : 0 ,
            'i' : 0 ,
            'o' : 0, 
            'u' : 0
        }
        temp = {
            (0,0,0,0,0) : -1
        }
        maxi = 0
        i = 0
        for  c in s :
            key = tuple(mymap.values())
            if c in mymap :
                mymap[c] += 1
                mymap[c] %= 2
                key = tuple(mymap.values())
                if key in temp :
                    maxi = max(maxi,i-temp[key])
                else :
                    temp[key]= i
            else :
                 maxi = max(maxi,i- temp[key])
            i+=1
        return maxi
