class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrom(s) :
            l = 0 
            r = len(s)-1 
            while l < r :
                if s[l]!= s[r] :
                    return False 
                l+=1 
                r-=1 
            return True
        n = len(s)
        res = []
        result = []
        def dfs(i) :
            if i == n :
                result.append(res[:])
                return 
            for j in range(i,n) :
                # print(s[i:j+1])
                if isPalindrom(s[i:j+1]) :
                    res.append(s[i:j+1])
                    dfs(j+1)
                    res.pop()
        dfs(0)
        return result





       

        