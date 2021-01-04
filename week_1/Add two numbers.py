# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2) :
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        temp = None
        head = None
        carry = 0   
        while(l1 is not None or l2 is not None):
 
            fdata = l1.val if l1 else 0
            sdata = l2.val if l2 else 0
            Sum = carry + fdata + sdata
 
            if Sum>= 10:
                carry=1
                Sum= Sum%10
            else:
                carry=0
                
            if head is None:
                head=ListNode(Sum)
                temp=head
            else:
                temp.next = ListNode(Sum)
                temp=temp.next
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
            
        if carry !=0:
            temp.next=ListNode(carry)
            
            
        return(head)
