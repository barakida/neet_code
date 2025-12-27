"""
Remove Node From End of Linked List
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:

You are given the beginning of a linked list head, and an integer n.
Remove the nth node from the end of the list and return the beginning of the list.

Example 1:
Input: head = [1,2,3,4], n = 2
Output: [1,2,4]

Example 2:
Input: head = [5], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 2
Output: [2]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

from typing import Optional

from neet_code.classes.linked_list_node import ListNode
from neet_code.utils.display_utils_utils import print_linkedlist_results

EXAMPLES = [
    {"input": {"head": [1, 2, 3, 4], "n": 2}, "output": [1, 2, 4]},
    {"input": {"head": [5], "n": 1}, "output": []},
    {"input": {"head": [1, 2], "n": 2}, "output": [2]},
]

COMPLEXITY = """

"""


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    root = ListNode(next_node=head)
    slow, fast = root, root

    for _ in range(n):
        fast = fast.next

    while fast.next:
        slow, fast = slow.next, fast.next

    slow.next = slow.next.next

    return root.next


function = removeNthFromEnd


if __name__ == '__main__':
    print_linkedlist_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
