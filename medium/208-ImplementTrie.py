"""
Complexity:
- Time  : O(n)
- Space : O(t) total node created
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


# Runtime: ms
# Memory Usage: MB
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for s in word:
            if s not in node.children:
                node.children[s] = TrieNode()
            node = node.children[s]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for s in word:
            if s not in node.children:
                return False
            node = node.children[s]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for s in prefix:
            if s not in node.children:
                return False
            node = node.children[s]
        return True


# Best time complexity solution (1ms)
class TrieBestTime:
    def __init__(self):
        self.root={}

    def insert(self, word: str) -> None:
        cur = self.root

        for letter in word:
            if letter not in cur:
                cur[letter]={}
            cur= cur[letter]
        cur['*']=''

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if letter not in cur:
                    return False
            cur=cur[letter]
        return '*' in cur
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur=cur[letter]
    
        return True 


# Best memory complexity solution (23.9MB)
class TrieBestMemory:
    def __init__(self):
        self.tree = []
        
    def insert(self, word: str) -> None:
        self.tree.append(word)
        

    def search(self, word: str) -> bool:
        if word in self.tree:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        for s in self.tree:
            if s.startswith(prefix):
                return True
        return False


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple")) # True
    print(trie.search("app")) # False
    print(trie.startsWith("app")) # True
    trie.insert("app")
    print(trie.search("app")) # True