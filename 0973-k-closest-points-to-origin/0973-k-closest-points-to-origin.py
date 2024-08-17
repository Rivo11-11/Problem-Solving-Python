class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for point in points :
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap,(dist,point[0],point[1]))
        
        res = []
        for i in range(k) :
           _,x,y = heapq.heappop(heap)
           res.append([x,y])
        return res
           


        