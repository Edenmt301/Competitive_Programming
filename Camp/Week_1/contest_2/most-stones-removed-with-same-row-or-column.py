from collections import deque
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        s = deque()
        count = 0
        visited = set()
        for stone in stones:
            if (stone[0],stone[1]) not in visited:
                s.appendleft((stone[0],stone[1]))
                visited.add((stone[0],stone[1]))
                currCount=0
                while(s):
                    curr = s.popleft()
                    currCount +=1
                    for i in stones:
                        if (i[0],i[1]) not in visited and (i[0] == curr[0] or i[1]== curr[1]):
                            s.appendleft((i[0],i[1]))
                            visited.add((i[0],i[1]))
                count += currCount-1
        return count
