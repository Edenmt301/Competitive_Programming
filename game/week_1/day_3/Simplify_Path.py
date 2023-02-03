class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        steps = path.split("/")
        print(steps)
        for step in steps:
            print(step)
            step = step.strip("/")
            if step == "..":
                if stack:
                    stack.pop()
                continue
            if step == ".":
                continue
            if step:
                stack.append( "/" + step)
        answer = "".join(stack)
        return "/" if not answer else answer 
            