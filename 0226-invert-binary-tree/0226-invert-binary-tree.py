# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def reverse(root) :
            if not root or ( not root.right and not root.left) :
              return 
            temp = root.left 
            root.left = root.right
            root.right = temp
            reverse(root.left)
            reverse(root.right)
        reverse(root)
        return root



        # # DFS Traversal 
        # def DFS_traversal(root) :
        #     if  not root  :
        #         return
        #     print(root.val)
        #     DFS_traversal(root.left)
        #     DFS_traversal(root.right)

        # # BFS Traversal
        # def BFS_traversal(root) :
        #     if not root :
        #         return 
        #     queue = deque()
        #     queue.append(root)
        #     while queue :
        #         node = queue.popleft()
        #         print(node.val)
        #         if node.left :
        #             queue.append(node.left)
        #         if node.right :
        #             queue.append(node.right)
            




 
        # DFS_traversal(root)
        # print("\n")
        # BFS_traversal(root)