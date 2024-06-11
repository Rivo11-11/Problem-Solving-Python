class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        myset = set(arr2) 
        temp = []
        mymap =  {}
        n1 = len(arr1)
        n2 = len(arr2)
        for i in range(n1) :
            if arr1[i] not in mymap :
                mymap[arr1[i]] = 1 
            else :
                mymap[arr1[i]] += 1
            if arr1[i] not in myset :
                temp.append(arr1[i])
        res = []
        for i in range(n2) :
            while mymap[arr2[i]] :
                res.append(arr2[i])
                mymap[arr2[i]] -= 1
        temp.sort()
        return res + temp



        