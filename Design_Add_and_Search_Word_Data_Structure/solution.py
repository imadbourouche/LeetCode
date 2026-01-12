class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        root = self.root
        for c in word: 
            if c not in root.children: 
                root.children[c] =  TrieNode()
            root = root.children[c]
        root.end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        def recv(word, node):
            for i in range(len(word)):
                c = word[i]
                if c == ".":
                    children = node.children.values()
                    for child in children:
                        if recv(word[i+1 :], child):
                            return True
                    return False
                elif c not in node.children:
                    return False
                node = node.children[c]
            return node.end_of_word
        return recv(word, node)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)