"""
Reverse Nodes in K-Group

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:

You are given the head of a singly linked list head and a positive integer k.
You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on.
If there are fewer than k nodes left, leave the nodes as they are.
Return the modified list after reversing the nodes in each group of k.

You are only allowed to modify the nodes' next pointers, not the values of the nodes.

Example 1:
Input: head = [1,2,3,4,5,6], k = 3
Output: [3,2,1,6,5,4]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
The length of the linked list is n.
1 <= k <= n <= 100
0 <= Node.val <= 100
"""
from typing import Optional

from neet_code.classes.linked_list_node import ListNode
from neet_code.utils.display_utils_utils import print_linkedlist_results

EXAMPLES = [
    {"input": {"head": [1,2,3,4,5,6], "k": 3}, "output": [3,2,1,6,5,4]},
    {"input": {"head": [1,2,3,4,5], "k": 3}, "output": [3,2,1,4,5]},
]

COMPLEXITY = """
O(n) time, O(1) extra space.
"""


def reverse_linked_list(head: ListNode) -> ListNode:
    root = ListNode(0)
    p1 = head
    while p1:
        temp = p1.next
        p1.next = root.next
        root.next = p1
        p1 = temp

    return root.next


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    root = ListNode(0, head)
    prev_end, curr_end = root, root

    while True:

        # isolate k values
        for _ in range(k):
            if not curr_end.next:
                return root.next
            curr_end = curr_end.next
        new_first = curr_end.next
        curr_end.next = None

        # reverse k values
        new_end = prev_end.next
        prev_end.next = reverse_linked_list(head=prev_end.next)
        new_end.next = new_first

        # prepare to ru again
        prev_end, curr_end = new_end, new_end


function = reverseKGroup


if __name__ == '__main__':
    print_linkedlist_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
