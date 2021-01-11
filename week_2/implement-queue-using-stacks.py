class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items1=[]
        self.items2=[]
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        length=len(self.items1)
        if length==0:
            self.items1.append(x)
        else:
            i=0
            while i < length:
                self.items2.append(self.items1.pop())
                i+=1
            self.items2.append(x)
            length=len(self.items2)
            i=0
            while i < length:
                self.items1.append(self.items2.pop())
                i+=1
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.items1)>0:
            return self.items1.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.items1)>0:
            return self.items1[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.items1)>0:
            return False
        else:
            return True
