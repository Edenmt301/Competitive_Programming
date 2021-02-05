class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        myHeap=[]
        if not lists:
            return
        for i in range (len(lists)) :
            current=lists[i]
            if not current:
                continue
            heapq.heappush(myHeap,[current.val,i])
        realRoot=None
        if myHeap:
            poped,index=heapq.heappop(myHeap)
            root=ListNode(poped)
            realRoot=root
            if lists[index].next:
                    lists[index]=lists[index].next
                    current=lists[index]
                    heapq.heappush(myHeap,[current.val,index])
                
        while myHeap:
            poped,index=heapq.heappop(myHeap)
            root.next=ListNode(poped)
            root=root.next
            if lists[index].next:
                lists[index]=lists[index].next
                current=lists[index]
                heapq.heappush(myHeap,[current.val,index])
        return realRoot
