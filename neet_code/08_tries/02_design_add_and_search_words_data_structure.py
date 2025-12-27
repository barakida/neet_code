"""
Design Add and Search Word Data Structure

class WordDictionary:

    def __init__(self):


    def addWord(self, word: str) -> None:


    def search(self, word: str) -> bool:

Design a data structure that supports adding new words and searching for existing words.
Implement the WordDictionary class:
void addWord(word) Adds word to the data structure.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
word may contain dots '.' where dots can be matched with any letter.
Example 1:

Input: ["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]
Output: [null, null, null, null, false, true, true, true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true
Constraints:

1 <= word.length <= 20
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 10,000 calls will be made to addWord and search.
"""

COMPLEXITY = """
Complexity

Let:
L = len(word) (≤ 20)
Σ = alphabet size = 26
d = number of dots (≤ 2)

addWord
Time: O(L)
Space: O(L) (new nodes if needed)

search
Worst case: O(Σ^d · L)
With d ≤ 2 → at most 26² = 676 branches → safe

This fits constraints comfortably.
"""


class LetterNode(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.word_end = False


class WordDictionary:
    def __init__(self):
        self.data = LetterNode()

    def addWord(self, word: str) -> None:
        data = self.data
        for l in word:
            data[l] = data.get(l, LetterNode())
            data = data[l]
        data.word_end = True

    def search(self, word: str) -> bool:

        def _search_word_tree(idx: int, word_tree: LetterNode) -> bool:
            if idx == len(word):
                return word_tree.word_end
            elif word[idx] == '.':
                return any(_search_word_tree(idx + 1, word_tree_) for word_tree_ in word_tree.values())
            elif word[idx] in word_tree:
                return _search_word_tree(idx + 1, word_tree[word[idx]])
            else:
                return False

        return _search_word_tree(0, self.data)




def main():
    word_dictionary = WordDictionary()
    word_dictionary.addWord("day")
    word_dictionary.addWord("bay")
    word_dictionary.addWord("may")
    print(f'word_dictionary.search("say")  |  result  {word_dictionary.search("say")} |  should return False')
    print(f'word_dictionary.search("day")  |  result  {word_dictionary.search("day")} |  should return True')
    print(f'word_dictionary.search(".ay")  |  result  {word_dictionary.search(".ay")} |  should return True')
    print(f'word_dictionary.search("b..")  |  result  {word_dictionary.search("b..")} |  should return True')

    print(f"\n{COMPLEXITY}")

if __name__ == '__main__':
    main()
