"""
Complexity:
- Time  : O(n)
- Space : O(n)
"""

class Solution:
    # Runtime: 11ms
    # Memory Usage: 17.32MB
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
 
        chars = []
        while x > 0:
            chars.append(x % 10)
            x = x // 10
        left = 0
        right = len(chars) - 1
        
        while left < right:
            if chars[left] != chars[right]:
                return False
            left = left + 1
            right = right - 1
        return True
            

    # Best time complexity solution (0ms)
    def isPalindromeBestTime(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0
        copy = x
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        return reverse == copy

    # Best memory complexity solution (17MB)
    def isPalindromeBestMemory(self, x: int) -> bool:
        temp = x
        reverse_no = 0
        while temp > 0:
            last_digit = temp % 10
            reverse_no = (reverse_no * 10) + last_digit
            temp = temp // 10
        return reverse_no == x 


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))

