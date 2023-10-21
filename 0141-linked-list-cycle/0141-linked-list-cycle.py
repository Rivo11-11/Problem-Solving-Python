# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        while curr : 
            ## Then there is a cycle
            if curr.val is None :
                return True
            ## Mark the visited node
            curr.val = None
            curr = curr.next
        return False
        