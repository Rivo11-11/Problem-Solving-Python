# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr = head 
        arr = []
        n = 0
        while curr :
            arr.append(curr.val)
            curr = curr.next
            n+=1
        temp = arr[k-1]
        arr[k-1] = arr[n-k]
        arr[n-k] = temp   
        res = ListNode(arr[0])
        head = res
        for i in range(1,n) :
            res.next = ListNode(arr[i]) 
            res = res.next
        return head
        
            
        
        