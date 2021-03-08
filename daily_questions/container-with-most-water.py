class Solution:
    def maxArea(self, height: List[int]) -> int:
        Left = 0
        Right = len(height)-1
        maxArea = 0
        
        while Left < Right:
            h =  min(height[Left], height[Right])
            w = Right-Left
            
            if w * h > maxArea:
                    maxArea = w * h
                    
            if height[Left] > height[Right]:
                Right -= 1
            else:
                Left += 1
        
        return maxArea   
