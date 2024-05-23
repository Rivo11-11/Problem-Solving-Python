# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        curr = head
        res = dummy
        while curr :
            if curr.val != val :
                dummy.next = curr
                dummy = dummy.next
            if not curr.next and curr.val == val :
                dummy.next = None
            curr = curr.next
        return res.next