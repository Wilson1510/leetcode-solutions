"""
Complexity:
- Time  : O(n)
- Space : O(n)
"""

class Solution:
    # Runtime: 3ms
    # Memory Usage: 20.66MB
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        longest = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    current_length = i - stack[-1]
                    longest = max(longest, current_length)
        return longest

    # Best time complexity solution (0ms)
    def longestValidParenthesesBestTime(self, s: str) -> int:
        stack=[-1]
        count=0
        for x in range(len(s)):
            if s[x]=="(":
                stack.append(x)
            else:
                stack.pop()
                if not stack:
                    stack.append(x)
                else:
                    count=max(count,x-stack[-1])
        return count

    # Best memory complexity solution (17.2MB)
    def longestValidParenthesesBestMemory(self, s: str) -> int:
        s = list(s)
        # s: ), (, ), (, ), )
        while True:
            i = 0
            change = False
            while i < len(s):
                curr = i
                if s[curr] == '(':
                    # search for closing
                    curr += 1
                    previous = 0
                    while curr < len(s) and isinstance(s[curr], int):
                        previous += s[curr]
                        curr += 1
                    if curr < len(s) and s[curr] == ')':
                        change = True
                        s = s[:i] + [2 + previous] + s[curr + 1:]
                i += 1

            if not change:
                maximum = 0
                for _s in s:
                    if isinstance(_s, int):
                        maximum = max(maximum, _s)
                return maximum

            # merge blocks
            i = 0
            while i < len(s):
                curr = i
                while curr < len(s) and isinstance(s[curr], int):
                    curr += 1
                if curr - i >= 2:
                    s = s[:i] + [sum(s[i:curr])] + s[curr:]
                i += 1


if __name__ == "__main__":
    s = Solution()

    print(s.longestValidParentheses("(()"))
    print(s.longestValidParentheses(")()())"))
    print(s.longestValidParentheses(""))
