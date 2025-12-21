def is_balanced(s: str) -> bool:

    # init helpers
    brackets_map = {"{": "}", "[": "]", "(": ")"}
    stack = list()

    # iterate over string
    for c in s:
        if c in brackets_map:
            stack.append(c)
        elif stack and brackets_map[stack[-1]] == c:
            stack.pop()
        else:
            return False

    # return result (true if stack is empty, else false)
    return len(stack) == 0


def main():
    s = "{}{[()]}"
    print(is_balanced(s))
    s = "{}{[())]}"
    print(is_balanced(s))
    s = "{}{[())]})"
    print(is_balanced(s))


if __name__ is "__main__":
    main()
