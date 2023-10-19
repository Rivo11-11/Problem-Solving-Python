class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        mystr = ""
        n = len(word1)
        m = len(word2)
        i,j,k = 0, 0 ,0
        
        while i < n and j < m :
            if k%2 == 0 :
                mystr +=word1[i]
                i+=1
                k+=1
            else :
                 mystr +=word2[j]
                 j+=1
                 k+=1
        while i < n :
               mystr +=word1[i]
               i+=1
        while j < m :
               mystr +=word2[j]
               j+=1

        return mystr
        