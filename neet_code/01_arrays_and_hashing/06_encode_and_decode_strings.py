"""
Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
def encode(strs: List[str]) -> str:
def decode(s: str) -> List[str]:

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""
from typing import List


EXAMPLES = [
    {"input": {"strs": ["neet", "code", "love", "you"]}, "output": ["neet","code","love","you"]},
    {"input": {"strs": ["we", "say", ":", "yes"]}, "output": ["we","say",":","yes"]},
]

COMPLEXITY = """
Complexity
Encoding: O(n⋅k) (where n = number of strings, k = avg length)
Decoding: O(m) (where m = length of encoded string)
Space: O(m)
"""


def encode(strs: List[str]) -> str:
    return ''.join([str(len(string)).zfill(3) + string for string in strs])


def decode(s: str) -> List[str]:
    result = list()
    idx = 0
    while idx < len(s):

        # get length
        length = int(s[idx: idx + 3])
        idx += 3

        # get message
        result.append(s[idx: idx + length])
        idx += length

    return result


def main():
    print("\nSolution")
    for example in EXAMPLES:
        inputs, outputs = example["input"], example["output"]
        print(f"|  examples = {str(inputs)}  |  expected_results = {outputs}  |  result = {decode(encode(**inputs))}  |")
    print(COMPLEXITY)


if __name__ == '__main__':
    main()
