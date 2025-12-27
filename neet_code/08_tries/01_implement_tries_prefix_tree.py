"""
Implement Trie (Prefix Tree)

class PrefixTree:

    def __init__(self):


    def insert(self, word: str) -> None:


    def search(self, word: str) -> bool:


    def startsWith(self, prefix: str) -> bool:

A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings.
Some applications of this data structure include auto-complete and spell checker systems.

Implement the PrefixTree class:

PrefixTree() Initializes the prefix tree object.
void insert(String word) Inserts the string word into the prefix tree.
boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:
Input: ["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]
Output: [null, null, true, false, true, null, true]

Explanation:
PrefixTree prefixTree = new PrefixTree();
prefixTree.insert("dog");
prefixTree.search("dog");    // return true
prefixTree.search("do");     // return false
prefixTree.startsWith("do"); // return true
prefixTree.insert("do");
prefixTree.search("do");     // return true

Constraints:
1 <= word.length, prefix.length <= 1000
word and prefix are made up of lowercase English letters.
"""

COMPLEXITY = """
Complexity
Let L = length of word/prefix

Operation	Time	Space
insert	    O(L)	O(L)
search	    O(L)	O(1)
startsWith	O(L)	O(1)

Overall space: O(total characters inserted)
Optimal for a Trie.
"""


class PrefixTree:

    def __init__(self):
        self.data = dict()
    def insert(self, word: str) -> None:
        data = self.data
        for l in word:
            if l not in data:
                data[l] = dict()
            data = data[l]
        data['EOW'] = True

    def search(self, word: str) -> bool:
        data = self.data
        for l in word:
            if l not in data:
                return False
            data = data[l]
        return 'EOW' in data
    def startsWith(self, prefix: str) -> bool:
        data = self.data
        for l in prefix:
            if l not in data:
                return False
            data = data[l]
        return True


def main():
    prefix_tree = PrefixTree()
    prefix_tree.insert("dog")
    print(f'prefix_tree.search("dog")  |  result  {prefix_tree.search("dog")} |  should return True')
    print(f'prefix_tree.search("do")  |  result  {prefix_tree.search("do")} |  should return False')
    print(f'prefix_tree.startsWith("do")  |  result  {prefix_tree.startsWith("do")} |  should return True')
    prefix_tree.insert("do")
    print(f'prefix_tree.search("do")  |  result  {prefix_tree.search("do")} |  should return True')

    print(f"\n{COMPLEXITY}")


if __name__ == '__main__':
    main()
