class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        summ = self.findSum(root)
        return self.findMax(root, 0, summ, root)[1] % ((10 ** 9) + 7)
    
    def findSum(self, curr):
        
        if curr.left and curr.right:
            return curr.val + self.findSum(curr.left) + self.findSum(curr.right)
        if curr.left:
            return curr.val + self.findSum(curr.left)
        if curr.right:
            return curr.val + self.findSum(curr.right)
        
        return curr.val
    
    def findMax(self, curr, maximum, summ, root):
        
        if not curr.left and not curr.right:
            if ((summ - curr.val) * curr.val) > maximum:
                maximum = ((summ - curr.val) * curr.val)
                return curr.val, maximum
        
        if curr.left and curr.right:
            left,maximum1 = self.findMax(curr.left, maximum, summ, root)
            right,maximum2 = self.findMax(curr.right, maximum, summ, root)
            down = curr.val + left + right
            maximum = max(maximum1, maximum2)
            
            if curr == root:
                return down, maximum
            if ((summ - down) * down) > maximum:
                maximum=((summ - down) * down) 
            return down, maximum
        
        if curr.left:
            child,maximum = self.findMax(curr.left, maximum, summ, root)
       
        if curr.right:
            child,maximum = self.findMax(curr.right, maximum, summ, root)
            
        down = curr.val + child
        if curr == root:
            return down, maximum
        if ((summ - down) * down) > maximum:
            maximum=((summ - down) * down)
        return down, maximum
     
