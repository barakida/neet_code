"""
Add Two Numbers
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.
The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.
Each of the nodes contains a single digit.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Return the sum of the two numbers as a linked list.

Example 1:
Input: l1 = [1,2,3], l2 = [4,5,6]
Output: [5,7,9]
Explanation: 321 + 654 = 975.

Example 2:
Input: l1 = [9], l2 = [9]
Output: [8,1]

Constraints:
1 <= l1.length, l2.length <= 100.
0 <= Node.val <= 9
"""

from typing import Optional

from neet_code.classes.linked_list_node import ListNode
from neet_code.utils.display_utils_utils import print_linkedlist_results

EXAMPLES = [
    {"input": {"l1": [1, 2, 3], "l2": [4, 5, 6]}, "output": [5, 7, 9]},
    {"input": {"l1": [9], "l2": [9]}, "output": [8, 1]},
]

COMPLEXITY = """
Complexity
O(n) time, O(1) extra space
"""


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    keep = 0
    l3 = ListNode()
    p1, p2, p3 = l1, l2, l3
    while p1 or p2:
        total = (p1.val if p1 else 0) + (p2.val if p2 else 0) + keep
        keep, value = total // 10, total % 10
        p3.next = ListNode(val=value)
        p1, p2, p3 = p1.next if p1 else None, p2.next if p2 else None, p3.next
    if keep:
        p3.next = ListNode(val=keep)

    return l3.next


function = addTwoNumbers


if __name__ == '__main__':
    print_linkedlist_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
