# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        nums = []
        current = head

        while current:
            nums.append(current.val)
            current = current.next
        

        nums = nums[::-1]


        dummy = ListNode(0)
        current = dummy

        for num in nums:
            current.next = ListNode(num)
            current = current.next

        return dummy.next
        
        