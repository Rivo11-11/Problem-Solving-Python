# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num = ''
        curr = head 
        while curr : 
            num += str(curr.val)
            curr = curr.next

        number = str(int(num) * 2)
        n = len(number)
        curr = head
        flag = False
        for i in range(n) : 
            if  curr   : 
                curr.val = int(number[i])
                last = curr
                curr = curr.next
            else :
                ## there will be a part to be added 
                flag =True
                break 
        if flag :
            while i < n:
                last.next = ListNode(int(number[i]))
                last = last.next
                i +=1
        return head
        

        