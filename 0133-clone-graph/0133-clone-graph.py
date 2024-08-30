"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        hashmap = {}
        def dfs(node) :
            
            ## it is visited before
            if node in hashmap :
                return hashmap[node]
            
            ## clone the node and mark as visited
            copy = Node(node.val)
            hashmap[node] = copy 

            for neighbor in node.neighbors :
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        if not node :
            return None
        return dfs(node)
