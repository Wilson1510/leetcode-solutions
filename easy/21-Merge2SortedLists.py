"""
Complexity:
- Time  : O(m + n)
- Space : O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.41MB
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101)
        current = dummy
        
        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next

    # Best time complexity solution (0ms)
    def mergeTwoListsBestTime(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next

    # Best memory complexity solution (16.8MB)
    def mergeTwoListsBestMemory(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        new_curr = new_list
        curr1 = list1
        curr2 = list2

        while curr1 or curr2:
            v1 = curr1.val if curr1 else float('inf')
            v2 = curr2.val if curr2 else float('inf')
            
            if v1 < v2:
                new_curr.next = curr1
                curr1 = curr1.next
            else:
                new_curr.next = curr2
                curr2 = curr2.next
            new_curr = new_curr.next
        
        return new_list.next


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    print(s.mergeTwoLists(l1, l2))

    l1 = None
    l2 = None

    print(s.mergeTwoLists(l1, l2))

    l1 = None
    l2 = ListNode(0)

    print(s.mergeTwoLists(l1, l2))
