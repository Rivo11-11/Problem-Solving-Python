class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.capacity = k 
        self.curr = 0
        self.rear = None
        self.front = None

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull() :
            return False

        new_node = Node(value) 
        if self.front == None :
            self.front = self.rear = new_node 
        else :
            self.rear.next = new_node 
            self.rear = new_node
        self.curr += 1
        return True
        
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty() :
            return False
        self.front = self.front.next
        if self.front == None :
            self.rear = None 
        self.curr -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.front :
            return self.front.data
        return -1

    def Rear(self):
        """
        :rtype: int
        """
        if self.rear :
            return self.rear.data 
        return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.front is None 

    def isFull(self):
        """
        :rtype: bool
        """
        return self.capacity == self.curr


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()