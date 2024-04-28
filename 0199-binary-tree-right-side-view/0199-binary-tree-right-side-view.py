# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def bfs(root):

            if not root:
                return
    
            queue = [[root,0]]
            res = [(root.val,0)]
            result = [root.val]

            while queue:
                temp = queue.pop(0)
                node = temp[0]
                level = temp[1]
                if node.left :
                    if res[-1][1] == level + 1 :
                        res.pop() 
                        result.pop()
                    res.append((node.left.val,level + 1))
                    result.append(node.left.val)
                    queue.append([node.left,level + 1])
                if node.right:
                    if res[-1][1] == level + 1 :
                        res.pop() 
                        result.pop()
                    res.append((node.right.val,level + 1))
                    result.append(node.right.val)
                    queue.append([node.right,level + 1])
            return result
        return bfs(root)

    

                