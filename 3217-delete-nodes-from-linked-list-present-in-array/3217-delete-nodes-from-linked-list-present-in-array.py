# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        myset = set(nums)
        prev = ListNode(-1)
        prev.next = head
        answer = prev
        curr = head 
        while curr :
            if curr.val in myset :
                prev.next = curr.next
            else :
                prev = curr
            curr = curr.next
        return answer.next