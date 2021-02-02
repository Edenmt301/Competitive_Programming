class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        newTree=None
        if not t1 and not t2:
            return
        elif t1 and t2:
            newTree=TreeNode(t1.val + t2.val)
            newTree.left=self.mergeTrees(t1.left, t2.left)
            newTree.right=self.mergeTrees(t1.right, t2.right)
        elif t1:
            newTree=TreeNode(t1.val)
            newTree.left=self.mergeTrees(t1.left,None)
            newTree.right=self.mergeTrees(t1.right,None)
        elif  t2:
            newTree=TreeNode(t2.val)
            newTree.left=self.mergeTrees(None,t2.left)
            newTree.right=self.mergeTrees(None,t2.right)
    
            
        return newTree
