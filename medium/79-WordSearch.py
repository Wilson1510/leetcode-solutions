"""
Complexity:
- Time  : O(m * 4^n) m is the size of board, n is length of word
- Space : O(n)
"""
from typing import List
from collections import Counter


class Solution:
    # Runtime: 1ms
    # Memory Usage: 19.68MB
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)

        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False

        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]
    
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    stack = [(r, c, 0, True)]
                    visited = set()

                    while stack:
                        curr_r, curr_c, idx, is_visiting = stack.pop()

                        if is_visiting:
                            visited.add((curr_r, curr_c))

                            if idx == len(word) - 1:
                                return True
                            
                            stack.append((curr_r, curr_c, idx, False))

                            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                                nr, nc = curr_r + dr, curr_c + dc
                                if (0 <= nr < rows and 0 <= nc < cols and 
                                    (nr, nc) not in visited and 
                                    board[nr][nc] == word[idx + 1]):
                                    stack.append((nr, nc, idx + 1, True))
                        else:
                            visited.remove((curr_r, curr_c))
                            
        return False

    # Best time complexity solution (42ms)
    def existBestTime(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        if len(word) > m*n:
            return False
        
        bc = Counter(sum(board,[]))
        for c,amount in Counter(word).items():
            if bc[c] < amount:
                return False
        if bc[word[0]]>bc[word[-1]]:
            word = word[::-1]
        
        def backtrack(row:int,col:int,cur_index:str):
            if cur_index == len(word):
                return True
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[cur_index]:
                return False
            
            temp = board[row][col]
            board[row][col]=''

            cond = backtrack(row-1,col,cur_index+1) or backtrack(row+1,col,cur_index+1)
            if cond or backtrack(row,col-1,cur_index+1) or backtrack(row,col+1,cur_index+1):
                return True
            
            board[row][col] = temp
            return False
        
        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0):
                    return True
        
        return False

    # Best memory complexity solution (16.6MB)
    def existBestMemory(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        
        def dfs(w_index, row, col):
            if w_index == len(word):
                return True
            
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or word[w_index] != board[row][col]:
                return False

            visited.add((row, col))
            
            top = dfs(w_index + 1, row - 1, col)
            right = dfs(w_index + 1, row, col + 1)
            bottom = dfs(w_index + 1, row + 1, col)
            left = dfs(w_index + 1, row, col - 1)

            visited.remove((row, col))

            if True in [top, right, bottom, left]:
                return True
            
            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(0, row, col):
                    return True

        return False


if __name__ == "__main__":
    s = Solution()

    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # True
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")) # True
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")) # False
