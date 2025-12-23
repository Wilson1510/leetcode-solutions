"""
Complexity:
- Time  : O(n)
- Space : O(n)
"""

class Solution:
    # Runtime: 2ms
    # Memory Usage: 17.25MB
    def myAtoi(self, s: str) -> int:
        chars = []

        for char in s:
            if char == " " and len(chars) == 0:
                continue
            elif char in ["+", "-"] and len(chars) == 0:
                chars.append(char)
                continue
            elif not char.isdigit():
                break

            chars.append(char)
        
        if len(chars) == 0 or (chars[0] in ["+", "-"] and len(chars) == 1):
            return 0
        
        if int("".join(chars)) > 2**31 - 1:
            return 2**31 - 1
        elif int("".join(chars)) < -2**31:
            return -2**31
        else:
            return int("".join(chars))
            

    # Best time complexity solution (0ms)
    def myAtoiBestTime(self, s: str) -> int:
        s = s.lstrip()
        if s is "":
            return 0

        positive = -1 if s[0] is '-' else 1
        if s[0] is '-' or s[0] is '+':
            s = s[1:]

        num = 0
        for x in s:
            try:
                num += int(x)
                num *= 10
            except ValueError:
                if num > 0:
                    break
                else:
                    return 0
        num //= 10 
        num *= positive

        if num < -2**31:
            return -2**31
        elif num > 2**31 - 1:
            return 2**31 - 1
        else:
            return num

    # Best memory complexity solution (17MB)
    def myAtoiBestMemory(self, s: str) -> int:
        i = 0
        n = len(s)
        res = 0
        sign = 1

        while i < n and s[i] == ' ':
            i += 1
        
        if i == n:
            return res
        
        if s[i] == '-':
            sign = -1
        if s[i] in '+-':
            i += 1
        
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            if res*sign > 2**31-1:
                return 2**31-1
        
            if res * sign < -2**31:
                return -2**31

        return res * sign


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("42"))
    print(s.myAtoi(" -042"))
    print(s.myAtoi("1337c0d3"))
    print(s.myAtoi("0-1"))
    print(s.myAtoi("words and 987"))
    print(s.myAtoi("  +0 123"))
