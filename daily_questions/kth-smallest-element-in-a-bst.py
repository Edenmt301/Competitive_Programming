class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        out=[]
        return self.findSmall(root, k, out)
    
    def findSmall(self, root, k, out):
        if len(out) >= k:
            return out[k-1]
        if root == None:
            return
        
        leftSide = self.findSmall(root.left, k, out)
        out.append(root.val)
        rightSide = self.findSmall(root.right, k, out)
        
        return leftSide if leftSide else rightSide
