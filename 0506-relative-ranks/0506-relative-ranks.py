class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        n = len(score)
        res = [0]*n
        heap = []
        for i in range(n) :
            heapq.heappush(heap,(-score[i],i)) 
        mymap = {
            1 : 'Gold Medal',
            2 : 'Silver Medal',
            3 :  'Bronze Medal'
         }
        count = 1
        while heap : 
            val,i = heapq.heappop(heap)
            if count in mymap :
                res[i] = mymap[count]
            else :
                res[i] = str(count)
            count +=1
        return res
