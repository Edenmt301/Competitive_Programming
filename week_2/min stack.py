class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk=[]
        self.min=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stk.append(x)
        if len(self.min)>0:
            self.min.append(min(x,self.min[-1]))
        else:
            self.min.append(x)
    def pop(self):
        """
        :rtype: None
        """
        self.stk.pop()
        self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]

    def getMin(self):
        """
        :rtype: int
        """
        
        return self.min[-1]
