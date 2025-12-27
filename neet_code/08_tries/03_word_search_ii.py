"""
Word Search II

def find_words(board: List[List[str]], words: List[str]) -> List[str]:

Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.
For a word to be present it must be possible to form the word with a path in the board with
horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:
Input:
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
],
words = ["bat","cat","back","backend","stack"]
Output: ["cat","back","backend"]

Example 2:
Input:
board = [
  ["x","o"],
  ["x","o"]
],
words = ["xoxo"]
Output: []

Constraints:
1 <= board.length, board[i].length <= 12
board[i] consists only of lowercase English letter.
1 <= words.length <= 30,000
1 <= words[i].length <= 10
words[i] consists only of lowercase English letters.
All strings within words are distinct.
"""

from typing import List, Optional

from neet_code.utils.display_utils_utils import print_results

EXAMPLES = [
    {"input": {"board": [
            ["a","b","c","d"],
            ["s","a","a","t"],
            ["a","c","k","e"],
            ["a","c","d","n"]
        ], "words": ["bat","cat","back","backend","stack"]}, "output": ["cat","back","backend"]},
    {"input": {"board": [
            ["x","o"],
            ["x","o"]
        ], "words": ["xoxo"]}, "output": []},
]

COMPLEXITY = """
Let:
M × N = board size
K = number of words
L = average length of a word
ΣL = total number of characters across all words

Time Complexity
Part	                        Complexity	            Notes
Build trie	                    O(ΣL)	                ΣL = total characters in all words
DFS from one cell	            O(4ᴸ)	                L = max word length
DFS over board (worst-case)	    O(M · N · 4ᴸ)	        M×N board
Trie pruning (remove)	        O(ΣL) (amortized)	    Each trie node deleted once
Total (worst-case)	            O(M · N · 4ᴸ)	        Standard Word Search II bound
Total (practical/avg)	        ≈ O(M · N · α)	        α = reduced branching due to pruning

Space Complexity
Component	            Complexity	    Notes
Trie storage	        O(ΣL)	        One node per character
DFS recursion stack	    O(L)	        Max depth = word length
Board marking	        O(1)	        In-place ("#")
Results list	        O(K)	        K = number of found words
Total space	            O(ΣL)	        Dominated by trie
"""


class LetterNode(dict):
    def __init__(self, ch: Optional[str] = None, parent: Optional["LetterNode"] = None, word: Optional[str] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ch = ch
        self.parent = parent
        self.word = word

    def remove(self) -> None:
        self.word = None
        self._remove()

    def _remove(self) -> None:
        if len(self) == 0 and self.word is None:
            if self.parent is not None:
                del self.parent[self.ch]
                self.parent._remove()


class WordDictionary:
    def __init__(self):
        self.data = LetterNode()

    def __repr__(self) -> str:
        return self.data.__repr__()

    def add(self, word: str) -> None:
        data = self.data
        for l in word:
            if l not in data:
                data[l] = LetterNode(ch=l, parent=data)
            data = data[l]
        data.word = word


def find_words(board: List[List[str]], words: List[str]) -> List[str]:

    # init word search
    results = list()
    rows, cols = len(board), len(board[0])

    def walk_board(letter_node: LetterNode, iy: int, ix: int) -> None:

        # get character
        ch = board[iy][ix]

        # stop condition
        if ch not in letter_node:
            return

        # found word
        letter_node = letter_node[ch]
        if letter_node.word is not None:
            results.append(letter_node.word)
            letter_node.remove()

        # test new directions
        board[iy][ix] = "#"
        if iy > 0 and board[iy - 1][ix] != '#':
            walk_board(letter_node, iy - 1, ix)
        if iy + 1 < rows and board[iy + 1][ix] != '#':
            walk_board(letter_node, iy + 1, ix)
        if ix > 0 and board[iy][ix - 1] != '#':
            walk_board(letter_node, iy, ix - 1)
        if ix + 1 < cols and board[iy][ix + 1] != '#':
            walk_board(letter_node, iy, ix + 1)
        board[iy][ix] = ch

    # prep word dictionary
    word_dictionary = WordDictionary()
    for word in words:
        word_dictionary.add(word)

    # iterate over board
    for iy_ in range(rows):
        for ix_ in range(cols):
            walk_board(letter_node=word_dictionary.data, iy=iy_, ix=ix_)

    return results


function = find_words

if __name__ == '__main__':
    print_results(examples=EXAMPLES, function=function, complexity=COMPLEXITY)
