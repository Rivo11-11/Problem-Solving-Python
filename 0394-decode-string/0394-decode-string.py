class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = ""
        for i in range(len(s)) :
            # print(stack)
            if s[i] == "]" :
                c = ""
                while stack[-1] != "[" :
                    c = stack.pop() + c
                stack.pop() ## pop([)
                number = ""
                while stack and stack[-1].isnumeric() :
                    number = stack.pop() + number
                c *= int(number)
                stack.append(c)

                
            else :
                stack.append(s[i])
        return ''.join(stack)
      


        