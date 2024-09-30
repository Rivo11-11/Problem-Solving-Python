class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack = []
        self.capacity = maxSize
        self.curr = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.curr < self.capacity :
             self.stack.append(x)
             self.curr += 1
        

    def pop(self):
        """
        :rtype: int
        """
        if self.curr == 0 : return -1
        self.curr -= 1
        return self.stack.pop()

        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if k > self.curr :
            k = self.curr
        for i in range(k) :
            self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)