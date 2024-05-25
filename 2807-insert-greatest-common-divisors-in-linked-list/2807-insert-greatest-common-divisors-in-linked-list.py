# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def gcd(a,b) :
            if b == 0 :
                return a 
            return gcd(b,a%b)
        curr = head.next
        prev = head
        while curr :
            node = ListNode(gcd(curr.val,prev.val))
            prev.next = node 
            node.next = curr 
            prev = curr 
            curr = curr.next
        return head