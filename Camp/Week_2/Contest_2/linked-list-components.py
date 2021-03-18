class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        root=head
        comp=0
        z=0
        while root:
            if root.val in G:
                z=1
                root=root.next
                continue
            if z==1:
                comp+=1
                z=0
            root=root.next
        if z==1:
            comp+=1
        return comp
