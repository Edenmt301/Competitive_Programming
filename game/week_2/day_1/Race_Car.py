from collections import deque

class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        queue = deque()
        queue.append([0, 0, 1])
        visited = set()
        visited.add((0, 1))

        while queue:
            instructions, position, speed = queue.popleft()
            if position == target:
                return instructions

            r_position , r_speed = position, -1 * (speed/ abs(speed))
            a_position , a_speed = position + speed, speed * 2
            
            if (r_position , r_speed) not in visited and (position + speed > target or (target > r_position + speed and speed < 0)):
                visited.add((r_position , r_speed))
                queue.append([instructions + 1, r_position , r_speed])
            if (a_position , a_speed) not in visited:
                visited.add((a_position , a_speed))
                queue.append([instructions + 1 ,a_position , a_speed])
