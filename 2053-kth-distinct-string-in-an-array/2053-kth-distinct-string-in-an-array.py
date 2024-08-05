class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        mymap = defaultdict(int) 
        for s in arr :
            mymap[s] += 1
        n = len(arr)
        start = 1
        myset = set()
        for i in range(n) :
            if mymap[arr[i]] == 1 :
                if start == k :
                    return arr[i]
                start +=1 
        return ""

