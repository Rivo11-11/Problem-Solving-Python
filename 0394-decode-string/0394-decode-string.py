class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        mymap = {
            "]" : "["
        }
        stack = []
        for c in s :
            ## if closing bracket
            if c  in mymap :
                target  = ''
                ## arrive to the open bracket
                while stack[-1] != mymap[c] :
                    target = stack.pop() + target
                ## pop the open bracket
                stack.pop()
                ## pop the number before it 
                num = ''
                while stack and stack[-1].isnumeric() :
                    num = stack.pop() + num
                target *= int(num)
                stack.append(target)
            
            else :
                stack.append(c)
        return ''.join(stack)

        