class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        ## a->b a/b = 2.0
        ## b->c b/c = 3.0
        graph = defaultdict(list) 
        i = 0
        for u, v in equations:
            graph[u].append((v, values[i]))
            graph[v].append((u, 1.0 / values[i]))
            i += 1
        ans  = []
        visited = set()
        self.mult = 1
        def dfs(src,dest) :
            if src not in graph or dest not in graph :
                return False
            if src == dest :
                return True
            for neighbour in graph[src] :
                if neighbour[0] not in visited :
                    visited.add(neighbour[0])
                    if dfs(neighbour[0],dest) :
                        self.mult *= neighbour[1]
                        return True   
                    visited.remove(neighbour[0])
            return False
        for querie in queries  :
            if not dfs(querie[0],querie[1]) :
                ans.append(-1)
            else :
                ans.append(self.mult)
            visited = set()
            self.mult = 1
        return ans


            
        