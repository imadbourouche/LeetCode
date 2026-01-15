class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self, word: str) -> None:
        root = self.root
        for i in word:
            if i not in root.children:
                root.children[i] = TrieNode()
            root = root.children[i]
        root.end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)
        
        ROWS, COLOUMNS, res = len(board), len(board[0]), []

        def dfs(node, r, l, word):
            if r < 0 or l < 0:
                return
            if r >= ROWS or l >= COLOUMNS or board[r][l] not in node.children:
                return
            if board[r][l] == "*":
                return
            node = node.children[board[r][l]]
            word += board[r][l]
            char_before = board[r][l]
            if node.end_of_word:
                res.append(word)
            board[r][l] = "*"
            dfs(node, r-1, l, word)
            dfs(node, r+1, l, word)
            dfs(node, r, l-1, word)
            dfs(node, r, l+1, word)
            board[r][l] = char_before

        for r in range(ROWS):
            for l in range(COLOUMNS):
                dfs(trie.root, r, l, "")

        return res