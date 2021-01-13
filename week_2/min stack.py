class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk=[]
        

    def push(self, x: int) -> None:
        self.stk.append(x)
        
            

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        min=self.stk[0]
        for i in self.stk:
            if i<min:
                min=i
        return min
