# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1,head)
        prev,curr =dummy , head
        while curr and curr.next :
            nextPair = curr.next.next 
            second = curr.next 

            prev.next = second
            second.next = curr
            curr.next = nextPair
            prev = curr
            curr = nextPair
        return dummy.next
        