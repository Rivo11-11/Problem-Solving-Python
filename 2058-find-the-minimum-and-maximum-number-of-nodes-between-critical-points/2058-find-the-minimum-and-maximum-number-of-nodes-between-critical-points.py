# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        index = 0 
        curr = head 
        prev = None
        res = []
        n = 0 
        mini = float('inf')
        while curr : 
            if prev and curr.next :
                if prev.val < curr.val > curr.next.val or  prev.val > curr.val < curr.next.val :
                    res.append(index)
                    if n > 0 :
                        mini = min(mini,index-res[n-1])
                    n += 1 
            prev = curr
            index += 1
            curr = curr.next
        if n < 2 :
            return [-1,-1] 
        else : 
            return [mini,res[n-1] - res[0]]
        