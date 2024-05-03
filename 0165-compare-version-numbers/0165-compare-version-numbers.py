class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1,v2 = version1 , version2
        n1 = len(v1) 
        n2 = len(v2)
        list1 = []
        list2 = []
        temp = ''
        for i in range(n1) : 
            if v1[i] == '.' :
                list1.append(int(temp))
                temp = ''
                continue
            temp += v1[i] 
        list1.append(int(temp))
        temp = ''
        for i in range(n2) : 
            if v2[i] == '.' :
                list2.append(int(temp))
                temp = ''
                continue
            temp += v2[i] 
        list2.append(int(temp))
        n1 = len(list1) 
        n2 = len(list2)
        i = 0 
        j = 0 
        while i < n1  or  j < n2 : 
            num1 = list1[i] if i < n1 else 0
            num2 = list2[j] if j < n2 else 0
            if num1 > num2 :
                return 1 
            if num2 > num1 :
                return -1 
            i+=1 
            j+=1
        return 0
            
        
      
        