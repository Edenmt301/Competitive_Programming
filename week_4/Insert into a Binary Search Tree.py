class Solution(object):
    def insertIntoBST(self, root, val, realroot=None):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            root=TreeNode(val)
        realroot=root
        if root.val<val and root.right:
            self.insertIntoBST(root.right,val,realroot)
        elif root.val>val and root.left:
            self.insertIntoBST(root.left,val,realroot)
        elif root.val<val and not root.right:
            root.right=TreeNode(val)
        elif root.val>val and not root.left:
            root.left=TreeNode(val)
        return realroot
