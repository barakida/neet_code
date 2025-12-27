"""
Merge K Sorted Linked Lists

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:

You are given an array of k linked lists "lists", where each list is sorted in ascending order.
Return the sorted linked list that is the result of merging all of the individual linked lists.

Example 1:
Input: lists = [[1,2,4],[1,3,5],[3,6]]
Output: [1,1,2,3,3,4,5,6]

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
0 <= lists.length <= 1000
0 <= lists[i].length <= 100
-1000 <= lists[i][j] <= 1000
"""
from typing import List, Optional

from neet_code.classes.linked_list_node import ListNode

EXAMPLES = [
    {"input": {"lists": [[1,2,4],[1,3,5],[3,6]]}, "output": [1,1,2,3,3,4,5,6]},
    {"input": {"lists": []}, "output": []},
    {"input": {"lists": [[]]}, "output": []},
]

COMPLEXITY = """
O(N log k)
"""


def merge_sorted_list(head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
    head3 = ListNode(0)
    p1, p2, p3 = head1, head2, head3
    while p1 and p2:
        if p1.val <= p2.val:
            p3.next = p1
            p1 = p1.next
        else:  # p1.val > p2.val
            p3.next = p2
            p2 = p2.next
        p3 = p3.next
    p3.next = p1 if p1 else p2

    return head3.next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:

    lists = [l for l in lists if l]
    if not lists:
        return None

    merged_lists = list()
    while len(lists) > 1:
        head1 = lists.pop()
        head2 = lists.pop()
        merged_lists.append(merge_sorted_list(head1=head1, head2=head2))

        if merged_lists and len(lists) < 2:
            merged_lists.extend(lists)
            lists = merged_lists
            merged_lists = list()

    return lists[0]


def main():
    for e in EXAMPLES:
        lists = [ListNode.linkedlist_from_list(l) for l in e["input"]["lists"]]
        results_expected = e["output"]
        results_actual = mergeKLists(lists=lists)
        print(f"expected: {results_expected}  |  actual: {results_actual.to_list() if results_actual else []}")


if __name__ == '__main__':
    main()
