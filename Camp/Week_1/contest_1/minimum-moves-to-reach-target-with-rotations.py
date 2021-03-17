class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        directions = [
            [(1, 0), (1, 0)],    #down
            [(0, 1), (0, 1)],    #right
            [(0, 0), (1, -1)],   #clockwise
            [(0, 0), (-1, 1)]    #counter-clockwise
        ]
        direction_check = [(1,0), (0,1), (1,0), (0,1)]
        start = ((0, 0), (0, 1))
        queue, visited = deque([start + (0,)]), {start}
        
        def validate(position):
            if (position[0] <= len(grid) - 1 and 
                position[1] <= len(grid) - 1 and 
                grid[position[0]][position[1]] == 0):
                return True
            return False 
        
        while queue:
            current = queue.popleft()
            if current[0] == (len(grid) - 1, len(grid) - 2):
                return current[2]
            
            invalid = 2 if current[0][1] == current[1][1] else 3
            
            for i in range(4):
                d, dc= directions[i], direction_check[i]
                new_tail = current[0][0] + dc[0], current[0][1] + dc[1]
                new_head = current[1][0] + dc[0], current[1][1] + dc[1]
                if i != invalid and validate(new_head) and validate(new_tail):
                    new_tail = current[0][0] + d[0][0], current[0][1] + d[0][1]
                    new_head = current[1][0] + d[1][0], current[1][1] + d[1][1]
                    new = new_tail, new_head
                    if new not in visited:
                        queue.append(new + (current[2] + 1,))
                        visited.add(new)
        return -1           
