class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        n1 = len(str1)
        n2 = len(str2) 
        if n2 > n1 : 
            str1,str2 = str2,str1
            n1,n2 = n2,n1
        for i in range(n2-1,-1,-1) :
            div = str2[0:i+1]
            temp = div
            flag = False
            while str1.startswith(temp)  :
                if temp == str2 :
                    flag = True
                if temp == str1  and flag:
                    return div 
                temp += div 
                
        return ''
