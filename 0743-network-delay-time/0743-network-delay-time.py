class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u,v,time in times :
            graph[u].append((v,time))
        
        min_times = {}
        heap = [(0,k)]
        while heap :
            time,node = heapq.heappop(heap) 
            if node not in min_times :
                min_times[node] = time
            else :
                continue
            for neighbour,t_neighbour in graph[node] :
                heapq.heappush(heap,(time + t_neighbour,neighbour))
        if len(min_times) == n :
            return max(min_times.values())
        return -1
        
