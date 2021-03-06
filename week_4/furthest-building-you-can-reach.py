class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        added=0
        current_ind=0
        diff=[]
        while added<ladders and current_ind+1<len(heights):
            if heights[current_ind]<heights[current_ind+1]:
                diff.append(heights[current_ind+1]-heights[current_ind])
                added+=1
            current_ind+=1
        
        heapq.heapify(diff)
        
        while bricks>=0 and current_ind+1<len(heights):
            if heights[current_ind]<heights[current_ind+1]:
                difference=(heights[current_ind+1]-heights[current_ind])
                if diff and difference>diff[0]:
                    bricks-=heapq.heappop(diff)
                    heapq.heappush(diff,difference)
                else:
                    bricks-=difference
            if bricks>=0:
                current_ind+=1
        return current_ind            
                    
