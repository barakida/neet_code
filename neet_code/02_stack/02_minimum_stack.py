"""
Minimum Stack
Design a stack class that supports the push, pop, top, and getMin operations.

class MinStack:
    def __init__(self):

    def push(self, val: int) -> None:

    def pop(self) -> None:

    def top(self) -> int:

    def getMin(self) -> int:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.

Example 1:
Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
Output: [null,null,null,null,0,null,2,1]
Explanation:
    MinStack minStack = new MinStack();
    minStack.push(1);
    minStack.push(2);
    minStack.push(0);
    minStack.getMin(); // return 0
    minStack.pop();
    minStack.top();    // return 2
    minStack.getMin(); // return 1

Constraints:
-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks.

"""

COMPLEXITY = """
Complexity
Time: O(n) — one pass through the string.
Space: O(n) — worst case, all opens on stack.
"""


class MinStack:
    def __init__(self):
        self.stack = list()
        self.min_stack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(val if not self.min_stack else min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None


def main():
    print("\nSolution")
    minStack = MinStack()
    print("minStack = MinStack()")
    minStack.push(1)
    print("minStack.push(1)")
    minStack.push(2)
    print("minStack.push(2)")
    minStack.push(0)
    print("minStack.push(0)")
    value = minStack.getMin()  # return 0
    print(f"minStack.getMin()  | returned {value} |  # should return 0")
    minStack.pop()
    print("minStack.pop()")
    value = minStack.top()  # return 2
    print(f"value = minStack.top()  | returned {value} |  # should return 2")
    value = minStack.getMin()  # return 1
    print(f"minStack.getMin()  | returned {value} |  # should return 1")

    print(COMPLEXITY)


if __name__ == '__main__':
    main()
