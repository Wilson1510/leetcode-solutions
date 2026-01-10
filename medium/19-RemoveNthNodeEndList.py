"""
Complexity:
- Time  : O(n^2)
- Space : O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.48MB
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            trace = current
            for _ in range(n):
                trace = trace.next
            if trace is None:
                prev.next = current.next
                return dummy.next
            prev = current
            current = current.next

    # Best time complexity solution (0ms)
    def removeNthFromEndBestTime(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    # Best memory complexity solution (16.9MB)
    def removeNthFromEndBestMemory(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        l,cur=0,head
        while cur:
            l+=1
            cur=cur.next
        if l==n:
            return head.next
        cur=head
        for _n in range(1,l-n):
            cur=cur.next
        cur.next=cur.next.next
        return head


if __name__ == "__main__":
    s = Solution()

    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)

    l2 = ListNode(1)

    l3 = ListNode(1)
    l3.next = ListNode(2)

    print(s.removeNthFromEnd(l1, 2))
    print(s.removeNthFromEnd(l2, 1))
    print(s.removeNthFromEnd(l3, 1))
