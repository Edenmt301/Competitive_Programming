class Solution(object):
    def reverser(self, head,result=None):
        tail=None
        current=head
        if not current:
            return None,None
        if current and not current.next:
            result  =current
            tail=current
            return tail,result
        
        res=self.reverser(head.next,result)
        result=res[1]
        res=res[0]
        res.next=current
        tail=current
        if tail==head:
            tail.next=None
        return tail,result
    
    def reverseList(self, head,result=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reverse=self.reverser(head,None)
        return reverse[1]
