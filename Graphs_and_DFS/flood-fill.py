class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        RemovedColor=image[sr][sc]
        n,m=len(image),len(image[0])
        image[sr][sc]=newColor
        visited=set()
        self.dfs(RemovedColor, image, sr, sc, n, m, newColor, visited)
        return image
    
    
    def dfs(self,RemovedColor,image,sr, sc, n, m, newColor, visited):
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        
        for i in directions:
            next_i = sr + i[0]
            next_j = sc + i[1]
            
            if 0<=next_i <n and 0<=next_j<m and image[next_i][next_j]==RemovedColor:
                node = (next_i , next_j)
            
                if node not in visited:
                    image[next_i][next_j] = newColor
                    visited.add(node)
                    self.dfs( RemovedColor ,image ,next_i ,next_j ,n ,m ,newColor, visited)
                                        
                
                
