class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        out=[]
        out=self.inTraverse(root,out)
        print(out)
        for i in range(len(out)-1):
            if out[i]<out[i+1]:
                continue
            else:
                return False
        return True
    def inTraverse(self,root,out=[]):
        if root==None:
            return
        self.inTraverse(root.left,out)
        out.append(root.val)
        self.inTraverse(root.right,out)
        return out
