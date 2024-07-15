# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        mymap = {}
        childs = set()
        root = None
        for node in descriptions :
            if node[0] not in mymap :
                if node[2] == 1 :
                    mymap[node[0]] = [node[1],None]
                else :
                    mymap[node[0]] = [None,node[1]]

            else :
                  if mymap[node[0]][0]  :
                    mymap[node[0]][1] = node[1]
                  else :
                    mymap[node[0]][0] = node[1]
            
            childs.add(node[1])
        for key in mymap.keys() :
            if key not in childs :
                root = key

        def build_tree(node_val):
            if node_val is None:
                return None
            node = TreeNode(node_val)
            if node_val in mymap:
                left_val, right_val = mymap[node_val]
                node.left = build_tree(left_val)
                node.right = build_tree(right_val)
            return node
        return build_tree(root)



        