"""
Complexity:
- Time  : O(n log(k))
- Space : O(k)
"""
from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Runtime: 7ms
    # Memory Usage: 22.99MB
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        min_heap = []

        for i, list in enumerate(lists):
            if list:
                heapq.heappush(min_heap, (list.val, i, list))
        
        dummy = ListNode()
        current = dummy

        while min_heap:
            _, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        return dummy.next

    # Best time complexity solution (19ms)
    def mergeKListsBestTime(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from operator import attrgetter
        all_elements = []
        for l in lists:
            e = l
            while e:
                all_elements.append(e)
                e = e.next

        if not len(all_elements):
            return None

        all_elements.sort(key=attrgetter('val'))

        for i, e in enumerate(all_elements[:-1]):
            e.next = all_elements[i+1]

        return all_elements[0] 

    # Best memory complexity solution (18.4MB)
    def mergeKListsBestMemory(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or not lists:
            return None
        while len(lists) > 1:
            mergedList = []

            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) <len(lists) else None
                mergedList.append(self.mergeTwoLists(l1, l2))
            lists = mergedList
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next


if __name__ == "__main__":
    s = Solution()

    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    print(s.mergeKLists([l1, l2, l3])) # 1->1->2->3->4->4->5->6
    print(s.mergeKLists([])) # []
    print(s.mergeKLists([None])) # []

    l1 = ListNode()
    l2 = ListNode(-1, ListNode(5))
    l3 = ListNode(1, ListNode(4, ListNode(6)))
    l4 = ListNode(4, ListNode(5, ListNode(6)))
    print(s.mergeKLists([l1, l2, l3, l4])) # -1->1->4->4->5->5->6->6
