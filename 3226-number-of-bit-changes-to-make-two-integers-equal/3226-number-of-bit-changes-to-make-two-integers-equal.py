class Solution(object):
    def minChanges(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def convert(n) :
            stack = []
            while n :
                if n%2 == 0 :
                    stack.append(0)
                else : stack.append(1)
                n //= 2
            return stack
        num1 = convert(n)
        num2 = convert(k) 
        if num1 == num2 :
            return 0 
        n2 = len(num2)
        n1 = len(num1)
        if n2 > n1 :
            return -1
        mymap = {}
        step = 0
        for i in range(n2) :
            mymap[i] = num2[i]
        for i in range(n1) :
            mimo = mymap[i] if i < n2 else 0
            if num1[i] != mimo and num1[i] == 0 :
                return -1
            elif num1[i] != mimo :
                step += 1
        return step

        