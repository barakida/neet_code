class ListNode:
    def __init__(self, val: int = None, next_node: "ListNode" = None):
        self.val = val
        self.next = next_node

    def __repr__(self) -> list:
        return str(linkedlist_to_list(self))

    @classmethod
    def linkedlist_from_list(cls, values: list) -> "ListNode":
        return list_to_linkedlist(values=values)

    def to_list(self) -> list:
        return linkedlist_to_list(head=self)


def list_to_linkedlist(values: list) -> ListNode:
    head = ListNode()
    node = head
    for v in values:
        node.next = ListNode(val=v)
        node = node.next
    head = head.next

    return head


def linkedlist_to_list(head: ListNode) -> list:
    result = list()
    node = head
    while node is not None:
        result.append(node.val)
        node = node.next

    return result
