class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None
        self.tail=None
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        current=self.head
        if not current:
            return -1
        if index==0 and self.head:
            return current.val
        else:
            for i in range (index):
                if current.next:
                    current=current.next
                else:
                    return -1
            return current.val
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if not self.head:
            self.head=ListNode(val)
            self.tail=self.head
        else:
            current=ListNode(val)
            current.next=self.head
            self.head=current

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head==None:
            self.head=ListNode(val)
            self.tail=self.head
        else:
            current=ListNode(val)
            self.tail.next=current
            self.tail=current

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        current=self.head
        prev=None
        if index==0:
            self.addAtHead( val)
        else:
            for i in range (index):
                prev=current
                if current!=self.tail:
                    current=current.next
                else:
                    if current==self.tail and i==index-1:
                        prev=current
                    else:
                        return
            new=ListNode(val)
            if prev==self.tail:
                self.tail.next=new
                self.tail=new
            else:
                temp=prev.next
                prev.next=new
                new.next=temp
            
            

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        current=self.head
        prev=None
        if index==0:
            if self.head==self.tail:
                self.head=None
                self.Tail=None
            else:
                self.head=self.head.next
        else:
            for i in range (index):
                prev=current
                if current!=self.tail:
                    current=current.next
                else:
                    if current==self.tail and i<index:
                        return
        
            if current==self.tail:
                self.tail=prev
                self.tail.next=None
            else:
                prev.next=current.next
