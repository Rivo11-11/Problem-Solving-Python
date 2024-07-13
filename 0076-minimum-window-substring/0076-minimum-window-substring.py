class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = len(set(t)) 
        have = 0 
        l,r = 0,0 
        n = len(s)
        mini = float('inf') 
        res = []
        mymap_t = {}
        mymap_s = {}
        for i in range(len(t)) :
            if t[i] not in mymap_t :
                mymap_t[t[i]] = 1 
            else : 
                mymap_t[t[i]] += 1 
        while r < n :
            if s[r] in mymap_t :
                if s[r] not in mymap_s :
                    mymap_s[s[r]] = 1 
                else :
                    mymap_s[s[r]] += 1 
                if mymap_s[s[r]] == mymap_t[s[r]] :
                    have +=1

            while have == need :
                if s[l] in mymap_s : 
                    mymap_s[s[l]] -= 1 
                    if mymap_s[s[l]] <  mymap_t[s[l]] :
                        have -= 1
                if r-l < mini :
                    mini = r - l 
                    res = [l,r]
                l+=1
            r+=1
        if res :
            return s[res[0] : res[1]+1]
        return ""




        