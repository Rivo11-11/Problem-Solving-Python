class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        heap_chairs = []
        n = len(times) 
        start,end = times[targetFriend]
        times.sort()
        for i in range(n) :
            heapq.heappush(heap_chairs,i)
        heap_leave = []
        for time in times :
            ## i need first to check if there is any guest would return chair
            ## pop until the heap to be increasing order
            while heap_leave and heap_leave[0][0] <= time[0] :
                _,chair = heapq.heappop(heap_leave) 
                heapq.heappush(heap_chairs,chair)
            chair  = heapq.heappop(heap_chairs)
            if time[0] == start :
                return chair 
            heapq.heappush(heap_leave,(time[1],chair))
        return -1