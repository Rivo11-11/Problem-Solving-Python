class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        mymap = defaultdict(list) 
        n = len(arr)
        if n == 0 : return []
        res = [0 for i in range(n)]
        for i in range(n) :
            mymap[arr[i]].append(i)
        rank = 1
        arr.sort()
        i = 0
        while i < n  :
                c = 0
                for index in mymap[arr[i]] :
                    res[index] = rank
                    c+=1
                rank+=1
                i+=c
        return res
