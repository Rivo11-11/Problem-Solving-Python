class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        def convert(num) :
            string = ''
            count = 0
            while num :
                if num % 2 == 0 :
                    string += '0'
                else :
                    string += '1'
                num /= 2
                count += 1
            return (string,count)
        
        s,n1 = convert(start)
        g,n2 = convert(goal)
        count = 0
        i,j = 0,0 
        while i < n1 or j < n2 :
            num1 = s[i] if i < n1 else '0'
            num2 = g[j] if j < n2 else '0'
            if num1 != num2 :
                count += 1
            i+=1
            j+=1
        return count
        