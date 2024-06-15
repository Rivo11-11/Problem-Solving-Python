class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        n = len(profits)
        res = []
        for i in range(n) :
            res.append([capital[i],profits[i]]) 
        res.sort()
        i = 0
        max_heap = []
        while k :
            while i < n and res[i][0] <= w :
                heapq.heappush(max_heap, -res[i][1])
                i += 1
            if not max_heap:
                break
            w += -heapq.heappop(max_heap)
            k -= 1
        return w


           
            
        