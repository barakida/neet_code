"""
A queue is an abstract data type that maintains the order in which elements were added to it,
allowing the oldest elements to be removed from the front and new elements to be added to the rear.
This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue
(i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.
In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:

1 x: Enqueue element  into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.
Input Format

The first line contains a single integer, , denoting the number of queries.
Each line  of the  subsequent lines contains a single query in the form described in the problem statement above. All three queries start with an integer denoting the query , but only query  is followed by an additional space-separated value, , denoting the value to be enqueued.

Constraints

It is guaranteed that a valid answer always exists for each query of type .
Output Format

For each query of type , print the value of the element at the front of the queue on a new line.

Sample Input

STDIN   Function
-----   --------
10      q = 10 (number of queries)
1 42    1st query, enqueue 42
2       dequeue front element
1 14    enqueue 42
3       print the front element
1 28    enqueue 28
3       print the front element
1 60    enqueue 60
1 78    enqueue 78
2       dequeue front element
2       dequeue front element
Sample Output

Explanation

Perform the following sequence of actions:

Enqueue ; .
Dequeue the value at the head of the queue, ; .
Enqueue ; .
Print the value at the head of the queue, ; .
Enqueue ; .
Print the value at the head of the queue, ; .
Enqueue ; .
Enqueue ; .
Dequeue the value at the head of the queue, ; .
Dequeue the value at the head of the queue, ; .
"""


class Queue:
    def __init__(self):
        self.stack_in = list()
        self.stack_out = list()

    def enqueue(self, value: float):
        self.stack_in.append(value)

    def _move_stack_in_to_out(self):
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())

    def dequeue(self) -> float:
        if not self.stack_out:
            self._move_stack_in_to_out()

        return self.stack_out.pop()

    def peek(self):
        if not self.stack_out:
            self._move_stack_in_to_out()

        print(self.stack_out[-1])


def main():

    queue = Queue()
    queue.enqueue(42)
    print(queue.dequeue())
    queue.enqueue(14)
    queue.peek()
    queue.enqueue(28)
    queue.peek()
    queue.enqueue(60)
    queue.enqueue(78)
    print(queue.dequeue())
    print(queue.dequeue())


if __name__ == '__main__':
    main()
