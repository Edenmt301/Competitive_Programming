class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        out=[]
        return self.postTraverse(root,out)
    def postTraverse(self,root,out):
        if root==None:
            return
        self.postTraverse(root.left,out)
        self.postTraverse(root.right,out)
        out.append(root.val)
        print(out)
        return out
