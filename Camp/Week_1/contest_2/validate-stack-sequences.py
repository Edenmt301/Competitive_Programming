class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        for i in popped:
            if i in pushed:
                x=pushed.index(i)
                for j in range(x+1):
                    stack.append(pushed.pop(0))
        
            if stack and stack[-1]==i:
                stack.pop(-1)
            else:
                return False
            
        return True
                    
