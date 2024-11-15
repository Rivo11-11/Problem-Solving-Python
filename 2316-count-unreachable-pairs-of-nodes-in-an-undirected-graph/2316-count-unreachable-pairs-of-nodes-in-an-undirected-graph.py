class Solution(object):
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        ## graph 
        graph = defaultdict(list) 
        for u,v in edges :
            graph[u].append(v)
            graph[v].append(u) 
        visited = set()
        self.visit_count = 0
        def dfs(node) :
                visited.add(node)
                self.visit_count += 1
                for neighbour in graph[node] :
                    if neighbour not in visited :
                        self.count += 1
                        dfs(neighbour)
                return self.count
        ans = []     
        prev = 0
        res = 0
        for node in graph :
            self.count = 0
            if node not in visited :
                now = (dfs(node)+1)
                res += now * prev 
                prev = now + prev
        rest = n - self.visit_count 
        ## relations between the nodes and themselves 
        res += rest * (rest - 1) // 2
        ## relations between the indvidual nodes and the block left
        res += prev * rest
        return res


