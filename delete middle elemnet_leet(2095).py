'''2095. Delete the Middle Node of a Linked List
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node.'''


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newnode=ListNode()
        newnode.next=head
        slow=newnode
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return newnode.next
