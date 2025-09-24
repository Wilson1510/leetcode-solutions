from typing import Optional

"""
Complexity:
- Time  : O(m + n)
- Space : O(m + n)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Runtime: 11 ms
    # Memory Usage: 17.97 MB
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        all_linked_lists = [l1, l2]
        sum = 0
        for linked_list in all_linked_lists:
            number = ""
            while True:
                number = number + str(linked_list.val)
                linked_list = linked_list.next
                if not linked_list:
                    break
            sum = sum + int(number[::-1])
        
        reverse_sum = str(sum)[::-1]

        dummy = ListNode(0)
        current = dummy

        for ch in reverse_sum:
            digit = int(ch)
            current.next = ListNode(digit)
            current = current.next

        return dummy.next 
    
    # Best time complexity solution (0 ms)
    def addTwoNumbersBestTime(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            current.next = ListNode((val1 + val2 + carry) % 10)

            carry = (val1 + val2 + carry) // 10

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            current = current.next

    # Best memory complexity solution (16.8 MB)
    def addTwoNumbersBestMemory(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #----Variables----
        carry = 0
        newlst_head = ListNode()
        current = newlst_head

        while l1 or l2 or carry:
            #Calculate values
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            #Generate total sum
            total_sum = value1+value2+carry

            #Extract the single digit, calculate what is carried
            single_digit = total_sum % 10
            carry = total_sum // 10

            #Create a new node, iterate
            current.next = ListNode(single_digit)
            current = current.next

            #Iterate if not empty
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        #Head points at 0, list starts at head.next, return head.next
        return newlst_head.next


if __name__ == "__main__":
    s = Solution()

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    s = s.addTwoNumbers(l1, l2)
    print(s.val)
    print(s.next.val)
    print(s.next.next.val)
