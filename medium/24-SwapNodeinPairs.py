"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        string = str(self.val)
        self = self.next
        while self:
            string += "->" + str(self.val)
            self = self.next
        return string

class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.33MB
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        current.next = head

        while current and current.next and current.next.next:
            first = current.next
            second = current.next.next

            current.next = second
            first.next = second.next
            second.next = first

            current = current.next.next

        return dummy.next

    # Best time complexity solution (0ms)
    def swapPairsBestTime(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node helps handle head swaps easily
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first

            # Move prev to the next pair
            prev = first

        return dummy.next

    # Best memory complexity solution (16.9MB)
    def swapPairsBestMemory(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first, second = head, head.next

        first.next = self.swapPairs(second.next)
        second.next = first

        return second


if __name__ == "__main__":
    s = Solution()

    print(s.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))) # 2->1->4->3
    print(s.swapPairs(ListNode(1, ListNode(2, ListNode(3))))) # 2->1->3
    print(s.swapPairs(ListNode(1))) # 1
    print(s.swapPairs(None)) # None
