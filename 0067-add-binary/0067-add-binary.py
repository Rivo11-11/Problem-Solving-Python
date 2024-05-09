class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n1 = len(a)
        n2 = len(b)
        l1 = n1 - 1
        l2 = n2 - 1 
        carry = 0
        stack = []
        while l1 >= 0 or l2 >= 0 :
            b1 = int(a[l1]) if l1 >= 0  else  0
            b2 = int(b[l2]) if l2 >= 0  else  0
            res = b1 + b2 + carry
            if res > 1 :
                res = 0 if res == 2 else 1
                carry = 1
            else :
                carry = 0
            stack.append(str(res))
            l1 -= 1
            l2 -= 1
        if carry :
            stack.append(str(carry))
        res = ''
        while stack  :
            res += stack.pop()
        return res
            
        
        