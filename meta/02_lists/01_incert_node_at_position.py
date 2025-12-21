"""
Given a pointer to the head node of a linked list and an integer to insert at a certain position,
create a new node with the given integer as its  attribute, insert this node at the desired position,
and return the head node.

A position of 0 indicates the head, a position of 1 indicates one node away from the head, and so on.
The head pointer given may be null, meaning that the initial list is empty.

Example
 refers to the first node in the list


Insert a node at position  with . The new list is

Function Description
Complete the function  with the following parameters:

: a reference to the head of the list
: an integer value to insert as data in the new node
: an integer position to insert the new node, zero-based indexing
Returns

: a reference to the head of the revised list

Input Format
The first line contains an integer , the number of elements in the linked list.
Each of the next  lines contains an integer SinglyLinkedListNode[i].data.
The next line contains an integer , the data of the node that is to be inserted.
The last line contains an integer .

Constraints

, where  is the  element of the linked list.
.
Sample Input

STDIN   Function
-----   --------
3       n = 3
16      llist = 16->13->7
13
7
1       data = 1
2       position = 2
Sample Output

16 13 1 7
Explanation

The initial linked list is . Insert  at the position  which currently has  in it. The updated linked list is .
"""

from typing import Any

from meta.utils.list_node import Node


def insert_node(head: Node, data: Any, position: int) -> Node:
    root = Node(0, head)
    p = root
    for _ in range(position):
        p = p.next
    p.next = Node(data, p.next)

    return root.next


def main():
    lst_in = [16, 13, 7]
    value = 1
    position = 2

    head = Node.from_list(lst_in)
    print(head.to_list())
    head = insert_node(head, value, position)
    print(head.to_list())


if __name__ == '__main__':
    main()
