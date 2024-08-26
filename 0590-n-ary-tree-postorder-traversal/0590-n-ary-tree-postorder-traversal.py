"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        def post(root) :
            for i in range(len(root.children)) :
                post(root.children[i])
            res.append(root.val)
        if root :
         post(root)
        return res

             
        