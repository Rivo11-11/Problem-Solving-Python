class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ## stack must be decreasing  else pop()
        n = len(temperatures) 
        res = [ 0 for i in range(n)]
        stack = []
        for i in range(n) :
            if not stack or temperatures[i] <= stack[-1][0] :
                stack.append((temperatures[i],i))
            else :
                while stack and temperatures[i] > stack[-1][0] :
                    _,index = stack.pop()
                    res[index] =  i - index 
                stack.append((temperatures[i],i))
            # print(stack)
            # print('----')
        return res
        
    
        