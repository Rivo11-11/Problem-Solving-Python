class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids:
            ## +ve (top of the stack) meet  -ve (next asteroid here a collusion will happen)
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    break 
                else:
                    break  
            else:
                stack.append(asteroid)
        
        return stack
    