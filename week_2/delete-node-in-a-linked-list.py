class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            current=node.next
            node.val=current.val
            node.next=current.next
        else:
            node=None
