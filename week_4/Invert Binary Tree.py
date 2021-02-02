class Solution(object):
    def invertTree(self, root ):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 
        if root.right and root.left:
            root.left,root.right=root.right,root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        elif root.right:
            root.left=root.right
            root.right=None
            self.invertTree(root.left)
        elif root.left:
            root.right=root.left
            root.left=None
            self.invertTree(root.right)
        return root
