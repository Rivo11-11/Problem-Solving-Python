class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        graph = defaultdict(list)
        i = 0
        for src,des in edges :
            graph[src].append((succProb[i],des)) 
            graph[des].append((succProb[i],src))
            i+=1 
        max_prob = {} 
        heap = [(-1,start_node)] 
        while heap :
            prob , node = heapq.heappop(heap) 
            prob = prob*-1
            if node in max_prob :
                continue
            max_prob[node] = prob
            for probability,neighbour in graph[node] :
                if neighbour in max_prob :
                    continue
                heapq.heappush(heap,(-probability*prob ,neighbour))
        if end_node in max_prob :
            return max_prob[end_node] 
        return 0
            

        