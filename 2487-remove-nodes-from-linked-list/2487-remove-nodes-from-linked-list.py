# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr  = head 
        stack = deque()
        while curr :
            if not stack or stack[-1] >= curr.val :
                stack.append(curr.val) 
            else :
                while stack and stack[-1] < curr.val :
                    stack.pop()
                stack.append(curr.val)
            curr = curr.next
            
        res = ListNode(stack.popleft())
        top = res
        while stack :
            res.next = ListNode(stack.popleft())
            res = res.next 
        return top
