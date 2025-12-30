"""
Word Search

def exist(board: List[List[str]], word: str) -> bool:

Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.
For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells.
The same cell may not be used more than once in a word.

Example 1:
Input:
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"
Output: true

Example 2:
Input:
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"
Output: false

Constraints:
1 <= board.length, board[i].length <= 5
1 <= word.length <= 10
board and word consists of only lowercase and uppercase English letters.
"""

from typing import List

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"board": [["A","B","C","D"],
                         ["S","A","A","T"],
                         ["A","C","A","E"]], "word": "CAT"}, "output": True},
    {"input": {"board": [["A","B","C","D"],
                         ["S","A","A","T"],
                         ["A","C","A","E"]], "word": "BAT"}, "output": False},
]

COMPLEXITY = """
Complexity Summary Table
Aspect	                Complexity	        Explanation
Time (worst case)	    O(R · C · 3^L)	    DFS from every cell, branching ≤ 3
Time (best case)	    O(1)	            Word found immediately
Recursion stack         O(L)	            Depth equals word length
Extra space	            O(1)	            Board modified in place
Output space	        O(1)	            Boolean result
"""


def exist(board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])


    def found_word(r: int, c: int, i: int) -> bool:
        if i == len(word):
            return True
        if not 0 <= r < rows or not 0 <= c < cols:
            return False
        if word[i] != board[r][c]:
            return False

        board[r][c] = "$"
        found = (found_word(r + 1, c, i + 1) or found_word(r, c + 1, i + 1) or
                 found_word(r - 1, c, i + 1) or found_word(r, c - 1, i + 1))
        board[r][c] = word[i]

        return found

    for row in range(rows):
        for col in range(cols):
            if found_word(row, col, 0):
                return True
    return False


function = exist


if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
