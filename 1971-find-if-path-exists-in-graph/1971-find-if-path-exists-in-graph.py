class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        adjList = defaultdict(list)
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
  
        visited = set()
        def dfs(node) :
            if node == destination:
                return True 
            if node in visited :
                return 

            visited.add(node) 
            for neighbour in adjList[node] :
                if dfs(neighbour) :
                    return True
            return False
        return dfs(source)
    
            