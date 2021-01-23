class Solution(object):
    def removeElements(self, head, val ):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        current=head
        if head and head.val==val:
                    if head.next:
                        while head.val==val:
                            head=head.next
                            if not head:
                                break
                    else:
                        head=None
        
        if not current or not current.next:
            return head
        
        if current.next.val==val:
            current.next=current.next.next
        else:    
            current=current.next
            
        self.removeElements(current,val)
        return head
