# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        current = dummy
        carry = 0

        # Traverse both lists
        while l1 or l2 or carry:
            # Get the values from l1 and l2; if one is None, use 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10

            # Create a new node for the current digit
            current.next = ListNode(new_digit)
            current = current.next

            # Move to the next nodes in l1 and l2
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the next node of dummy, which is the actual head of the resulting list
        return dummy.next
