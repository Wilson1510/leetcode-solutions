"""
Complexity:
- Time  : O(mnl^4)
- Space : O(wl)
"""
from typing import List


class Solution:
    # Runtime: 435ms
    # Memory Usage: 20.7MB
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Bangun Trie
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['$'] = word # Simpan kata langsung di node terakhir

        res = []
        rows, cols = len(board), len(board[0])

        def dfs(r, c, parent):
            char = board[r][c]
            curr_node = parent[char]

            # Cek apakah kita menemukan kata
            word_match = curr_node.pop('$', None)
            if word_match:
                res.append(word_match)

            # Tandai board agar tidak dikunjungi ulang (Backtracking)
            board[r][c] = '#'
            
            # Cek 4 arah
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node:
                    dfs(nr, nc, curr_node)
            
            # Kembalikan karakter asli
            board[r][c] = char

            # Optimasi: Hapus node jika sudah kosong (Pruning)
            if not curr_node:
                parent.pop(char)

        # 2. Iterasi setiap sel di board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    dfs(r, c, trie)
                    
        return res
    # Best time complexity solution (264ms)
    def findWordsBestTime(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        trie = {}
        for word in words:
            cur = trie
            for c in word:
                if not c in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["$"] = word

        res = []

        def dfs(trie, i, j):
            c = board[i][j]
            board[i][j] = "#"

            nxt = trie[c]
            if "$" in nxt:
                res.append(nxt["$"])
                nxt.pop("$")

            ip1, im1 = i + 1, i - 1
            jp1, jm1 = j + 1, j - 1
            if ip1 < n and board[ip1][j] in nxt:
                dfs(nxt, ip1, j)
            if i > 0 and board[im1][j] in nxt:
                dfs(nxt, im1, j)
            if jp1 < m and board[i][jp1] in nxt:
                dfs(nxt, i, jp1)
            if j > 0 and board[i][jm1] in nxt:
                dfs(nxt, i, jm1)

            if not nxt:
                trie.pop(c)

            board[i][j] = c

        for i in range(n):
            for j in range(m):
                if board[i][j] not in trie:
                    continue
                dfs(trie, i, j)
        return res

    # Best memory complexity solution (17.6MB)
    def findWordsBestMemory(self, board: List[List[str]], words: List[str]) -> List[str]:
        def exist(word: str) -> bool:
            m, n = len(board), len(board[0])
            length = len(word)
            def dfs(i: int, j: int, index: int) -> bool:
                if index == length - 1:
                    return True

                temp = board[i][j]
                board[i][j] = '#'
                if i > 0 and board[i - 1][j] == word[index + 1] and dfs(i - 1, j, index + 1):
                    board[i][j] = temp
                    return True
                if i < m - 1 and board[i + 1][j] == word[index + 1] and dfs(i + 1, j, index + 1):
                    board[i][j] = temp
                    return True
                if j > 0 and board[i][j - 1] == word[index + 1] and dfs(i, j - 1, index + 1):
                    board[i][j] = temp
                    return True
                if j < n - 1 and board[i][j + 1] == word[index + 1] and dfs(i, j + 1, index + 1):
                    board[i][j] = temp
                    return True
                
                board[i][j] = temp  
                return False

            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        if dfs(i, j, 0):
                            return True
            
            return False
        
        result = []
        board_count = {}
        for row in board:
            for letter in row:
                board_count[letter] = board_count.get(letter, 0) + 1

        for word in words:
            word_count = {}
            for letter in word:
                word_count[letter] = word_count.get(letter, 0) + 1
            legit = True
            for letter in word:
                if word_count[letter] > board_count.get(letter, 0):
                    legit = False
                    break
            if not legit:
                continue

            reverse = False
            if board_count[word[-1]] < board_count[word[0]]: #prejudge
                word = word[::-1]
                reverse = True

            if exist(word):
                if reverse:
                    result.append(word[::-1])
                else:
                    result.append(word)
        
        return result


if __name__ == "__main__":
    s = Solution()

    print(s.findWords(
        [
            ["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]
        ], ["oath","pea","eat","rain"]
    )) # ["eat","oath"]
    print(s.findWords(
        [
            ["a","b"],
            ["c","d"]
        ], ["abcb"]
    )) # []

    print(s.findWords(
        [
            ["m","b","c","d","e","f","g","h","i","j","k","l"],
            ["n","a","a","a","a","a","a","a","a","a","a","a"],
            ["o","a","a","a","a","a","a","a","a","a","a","a"],
            ["p","a","a","a","a","a","a","a","a","a","a","a"],
            ["q","a","a","a","a","a","a","a","a","a","a","a"],
            ["r","a","a","a","a","a","a","a","a","a","a","a"],
            ["s","a","a","a","a","a","a","a","a","a","a","a"],
            ["t","a","a","a","a","a","a","a","a","a","a","a"],
            ["u","a","a","a","a","a","a","a","a","a","a","a"],
            ["v","a","a","a","a","a","a","a","a","a","a","a"],
            ["w","a","a","a","a","a","a","a","a","a","a","a"],
            ["x","y","z","a","a","a","a","a","a","a","a","a"]
        ], [
            f"{char}{char2}aaaaaaaa" for char in "abcdefghijklmnopqrstuvwxyz" for char2 in "abcdefghijklmnopqrstuvwxyz"
        ]
    ))
