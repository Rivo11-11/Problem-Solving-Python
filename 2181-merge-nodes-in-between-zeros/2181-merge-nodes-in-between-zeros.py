# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode(0) 
        index = res
        prev = head 
        curr = head 
        s = 0
        while curr : 
            s += curr.val
            if curr.val == 0  : 
                prev = curr
                index.next = ListNode(s) 
                s = 0
                index = index.next
            curr = curr.next 
        return res.next.next

        