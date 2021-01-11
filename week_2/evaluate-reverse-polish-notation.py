class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            
            if i in '+-*/':
                result=0
                b=int(stack.pop())
                a=int(stack.pop())
                if i=='+':
                    result= a + b
                elif i=='-':
                    result= a - b    
                elif i=='*':
                    result= a * b    
                else:
                    if (a<0 and b<0) or (a>=0 and b>=0):
                        result= a // b
                    else:
                        result= math.ceil(a / b)
                    
                stack.append(str(result))
            else:
                stack.append(i)
        return stack.pop()
