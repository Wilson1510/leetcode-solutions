"""
Complexity:
- Time  : O(n)
- Space : O(n)
"""

class Solution:
    # Runtime: 12ms
    # Memory Usage: 17.43MB
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for _ in range(numRows)]
      
        # current_row: tracks which row we're currently adding to
        # direction: determines if we're moving down (1) or up (-1) in the zigzag
        current_row = 0
        direction = -1
      
        for char in s:
            rows[current_row].append(char)
          
            # Change direction when we reach the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                direction = -direction
          
            current_row += direction
      
        # Concatenate all rows together to form the final string
        # Using list comprehension to join each row, then join all rows
        return ''.join(''.join(row) for row in rows)


    # Best time complexity solution (2ms)
    def convertBestTime(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        row = [""] * numRows
        flag = True
        idx = 0

        for c in s:
            row[idx] += c
            if idx == 0 or idx == numRows - 1:
                flag = not flag
            if flag:
                idx -= 1
            else:
                idx += 1
        return ''.join(row)

    # Best memory complexity solution (16.6MB)
    def convertBestMemory(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        row_bucket = 0
        direction = 1  # 1 = down, -1 = up
        rows = [""] * numRows  # Initialize empty buckets

        for char in s:
            rows[row_bucket] += char  # Add to current row
            if row_bucket == numRows - 1:  # Hit bottom row?
                direction = -1  # Start moving up
            elif row_bucket == 0:  # Hit top row?
                direction = 1   # Start moving down
            row_bucket += direction  # Update row
        
        return "".join(rows)


if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))
    print(s.convert("PAYPALISHIRING", 4))
    print(s.convert("A", 1))