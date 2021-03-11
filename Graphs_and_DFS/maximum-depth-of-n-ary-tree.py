class Solution:
    def maxDepth(self, root: 'Node') -> int:
        maxi = 0
        count = 0
        if root:
            return self.dfs(root, maxi, count)
        return maxi
        
        
    def dfs(self, root, maxi, count):
        count += 1
        maxi = max(maxi, count)
        
        for each in root.children:
            maxi = self.dfs(each, maxi, count)
            
        return maxi
    
    
