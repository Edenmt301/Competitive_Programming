class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        temp=root
        if not temp:
            return 
        if temp.val==val:
            return temp
        if temp.val>val:
            temp=temp.left
        else:
            temp=temp.right
        result=self.searchBST(temp,val)
        return result
