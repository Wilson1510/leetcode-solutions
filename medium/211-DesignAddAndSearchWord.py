"""
Complexity:
- Time  : O(n)
- Space : O(n + t) t = total nodes created
"""


# Runtime: 782ms
# Memory Usage: 55.3MB
class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = True  # Menggunakan '$' lebih ringan daripada objek tambahan

    def search(self, word: str) -> bool:
        # Gunakan fungsi internal dengan indeks 'i' agar tidak ada slicing string
        def dfs(i, curr_node):
            for j in range(i, len(word)):
                char = word[j]
                if char == ".":
                    # Cek semua anak
                    for child in curr_node:
                        # Skip penanda akhir kata '$' saat iterasi titik
                        if child != '$' and dfs(j + 1, curr_node[child]):
                            return True
                    return False
                else:
                    if char not in curr_node:
                        return False
                    curr_node = curr_node[char]
            return '$' in curr_node

        return dfs(0, self.trie)


# Best time complexity solution (48ms)
class WordDictionary:
    __slots__ = ("next_id", "word_id", "full", "pos", "exact")

    def __init__(self):
        self.next_id = [0] * 26               # per-length next id
        self.word_id = {}                     # word -> per-length id (reuse)
        self.full = [0] * 26                  # full[L] bitmask of all ids of length L

        # preallocated bitset table: pos[L][i][ch] -> mask
        self.pos = [None] * 26
        for L in range(1, 26):
            self.pos[L] = [[0] * 26 for _ in range(L)]

        self.exact = [set() for _ in range(26)]  # exact[L] contains words of length L

    def addWord(self, w: str) -> None:
        L = len(w)
        if w in self.word_id:
            return

        self.exact[L].add(w)

        k = self.next_id[L]
        self.next_id[L] = k + 1
        self.word_id[w] = k

        bit = 1 << k
        self.full[L] |= bit

        table = self.pos[L]
        for i, c in enumerate(w):
            table[i][ord(c) - 97] |= bit

    def search(self, w: str) -> bool:
        L = len(w)

        if '.' not in w:
            return w in self.exact[L]

        m = self.full[L]
        if not m:
            return False

        table = self.pos[L]
        for i, c in enumerate(w):
            if c != '.':
                m &= table[i][ord(c) - 97]
                if not m:
                    return False
        return True


# Best memory complexity solution (24.75MB)
class WordDictionary:

    def __init__(self):
        self.hash_map = {}

    def addWord(self, word: str) -> None:
        self.hash_map[word] = True

    def search(self, word: str) -> bool:
        if word in self.hash_map: return True
        index = word.find('.')
        if index == -1 : return False
        ret = False
        def compareStrings():
            if len(word) != len(word2):
                return False
            for i in range(len(word)):
                if word[i] != '.' and word[i] != word2[i]:
                    return False
            return True
        for word2 in self.hash_map:
            if compareStrings():
                ret = True
                break
        return ret


if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad")) # False
    print(wordDictionary.search("bad")) # True
    print(wordDictionary.search(".ad")) # True
    print(wordDictionary.search("b..")) # True
