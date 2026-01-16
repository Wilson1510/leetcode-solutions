"""
Complexity:
- Time  : O(n)
- Space : O(n)
"""

class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.31MB
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in pairs:
                top_element = stack.pop() if stack else '#'
                
                if pairs[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

    # Best time complexity solution (0ms)
    def isValidBestTime(self, s: str) -> bool:
        stack =[]
        mapping = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for ch in s:
            if ch in mapping:
                if not stack or stack[-1]!=mapping[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack

    # Best memory complexity solution (16.9MB)
    def isValidBestMemory(self, s: str) -> bool:
        i=0
        a=[]
        for i in range(len(s)):
            if s[i]=='('or s[i]=='['or s[i]=='{':
                a.append(s[i])
            else:
                if not a:
                    return False
                top=a.pop()
                if s[i]==')'and top!='(':
                    return False
                if s[i]==']'and top!='[':
                    return False
                if s[i]=='}'and top!='{':
                    return False
        return len(a)==0


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))  # true
    print(s.isValid("()[]{}"))  # true
    print(s.isValid("(]"))  # false
    print(s.isValid("([])"))  # true
    print(s.isValid("([)]"))  # false
    print(s.isValid("{[]}"))  # true
    print(s.isValid("["))  # false
    print(s.isValid("]"))  # false
    print(s.isValid("(()[]{}[(){[]}])"))  # true
    print(s.isValid("(([]){})"))  # true
