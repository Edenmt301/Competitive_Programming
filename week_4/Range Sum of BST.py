class Solution(object):
    def rangeSumBST(self, root, low, high,summ=0):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        
        if root.val<low: 
            summ+=self.rangeSumBST(root.right, low, high)
        elif root.val>high: 
            summ+=self.rangeSumBST(root.left, low, high)
        elif root.val>=low and root.val<=high:
            summ+=root.val
            summ+=self.rangeSumBST(root.left, low, high)
            summ+=self.rangeSumBST(root.right, low, high)
        return summ
