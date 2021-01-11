class RecentCounter:

    def __init__(self):
        
        self.stack=[]
        self.milsec=0

    def ping(self, t: int) -> int:
        count=0
        self.stack.append(t)
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i] >=t-3000:
                count+=1
            else:
                break
        return count
