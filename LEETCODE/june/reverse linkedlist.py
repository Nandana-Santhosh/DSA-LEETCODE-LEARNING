'''206. Reverse Linked List
Solved
Easy
Topics
Companies
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]'''


    class Solution:
        def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            curr,prev = head ,None
            while curr is not None:
                temp = curr.next
                curr.next = prev
                prev, curr = curr,temp
            return prev
                