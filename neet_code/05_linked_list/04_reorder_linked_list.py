"""
Reorder Linked List
def reorderList(head: Optional[ListNode]) -> None:

You are given the head of a singly linked-list.
The positions of a linked list of length = 7 for example, can intially be represented as:
[0, 1, 2, 3, 4, 5, 6]
Reorder the nodes of the linked list to be in the following order:
[0, 6, 1, 5, 2, 4, 3]
Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:
Input: head = [2,4,6,8]
Output: [2,8,4,6]

Example 2:
Input: head = [2,4,6,8,10]
Output: [2,10,4,8,6]

Constraints:
1 <= Length of the list <= 1000.
1 <= Node.val <= 1000
"""

from typing import Optional

from neet_code.classes.linked_list_node import ListNode
from neet_code.utils.display_utils_utils import print_linkedlist_results

EXAMPLES = [
    {"input": {"head": [2, 4, 6, 8]}, "output": [2, 8, 4, 6]},
    {"input": {"head": [2, 4, 6, 8, 10]}, "output": [2, 10, 4, 8, 6]},
]

COMPLEXITY = """
Complexity
Time: O(n) (one pass to find middle, one to reverse, one to merge).
Space:  O(1) extra — pointers only.
"""


def reorderList(head: Optional[ListNode]) -> None:
    # edge case
    if not head or not head.next:
        return head

    # split list
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    head1, head2 = head, slow.next
    slow.next = None

    # reverse sub-list
    prev_node, current_node = None, head2
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    head2 = prev_node

    # join lists
    p1, p2 = head1, head2
    while p2:
        p3 = p1.next
        p1.next = p2
        p2 = p3
        p1 = p1.next

    head = head1

    return head


function = reorderList


if __name__ == '__main__':
    print_linkedlist_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)


"""

    # find middle
    fast, slow = head, head
    temp = None
    while fast and fast.next:
        temp = slow
        slow = slow.next
        fast = fast.next.next
    if temp:
        temp.next = None

    # reverse second half
    prev, current = None, slow
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    head_2 = prev

    # merge lists
    root = ListNode()
    current, current_1, current_2 = root, head, head_2
    while current_1:
        current.next = current_1
        current = current.next
        current_1 = current_1.next

        if current_2:
            current.next = current_2
            current = current.next
            current_2 = current_2.next

    return head
"""