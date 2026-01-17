"""
Complexity:
- Time  : O()
- Space : O()
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
    # Runtime: ms
    # Memory Usage: MB
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKthNode(current, k):
            while current and k > 1:
                current = current.next
                k -= 1
            return current
        
        current = head
        dummy = ListNode(0)
        dummy.next = head
        
        while current and current.next:
            kth = getKthNode(current, k)
            print(f"kth: {kth}")
            if not kth:
                break

            penanda_kth = kth.next
            first = current

            while current != kth.next:
                temp = current
                print(f"t: {temp}, {kth.next}")
                current = temp.next
                print(f"c: {current}")
                temp.next = penanda_kth
                print(f"tp: {temp.next}")
                penanda_kth = temp
                print(f"pk: {penanda_kth}")


            step = current
            for i in range(k-1):
                step = step.next

            first.next = step
                
        # return dummy.next
            

    # Best time complexity solution (ms)
    def reverseKGroupBestTime(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass

    # Best memory complexity solution (MB)
    def reverseKGroupBestMemory(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass


if __name__ == "__main__":
    s = Solution()

    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(s.reverseKGroup(l, 3)) # 3->2->1->4->5
    print(s.reverseKGroup(l, 2)) # 2->1->4->3->5
