def findMergeNode(head1, head2):
    stack1=[]
    current1=head1
    while current1:
        stack1.append(current1)
        current1=current1.next
        
    stack2=[]
    current2=head2
    while current2:
        stack2.append(current2)
        current2=current2.next
    
    prev=-1
    for i in range(len(stack2)):
        if len(stack1)!=0 and len(stack2)!=0:
            one = stack1.pop()
            two = stack2.pop()
            if one==two:
                prev =one.data
            else:
                break
            continue
        break
    return prev
