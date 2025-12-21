class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    @classmethod
    def from_list(cls, values: list) -> 'Node':
        root = Node(0)
        p = root
        for v in values:
            p.next = Node(v)
            p = p.next
        return root.next

    def to_list(self) -> list:
        lst = []
        p = self
        while p:
            lst.append(p.data)
            p = p.next
        return lst
