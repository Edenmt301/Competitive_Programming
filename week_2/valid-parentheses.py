class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            else:
                if len(stack)!=0:
                    if i==')' and stack.pop()=='(':
                        continue
                    elif i=='}' and stack.pop()=='{':
                        continue   
                    elif i==']' and stack.pop()=='[':
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
