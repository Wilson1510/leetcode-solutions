"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""

class Solution:
    # Runtime: 42ms
    # Memory Usage: 17.27MB
    def reverse(self, x:int) -> int:
        rev = 0
        is_negative = x < 0

        MIN_INT = -2**31
        MAX_INT = 2**31 - 1

        x = abs(x)

        while x != 0:
            last_digit = x % 10

            if (rev > MAX_INT / 10) or (rev == MAX_INT / 10 and last_digit > 7):
                return 0
            elif (rev < MIN_INT / 10) or (rev == MIN_INT / 10 and last_digit < -8):
                return 0

            rev = rev * 10 + last_digit

            x = x // 10

        return rev if not is_negative else -rev
        

    # Best time complexity solution (0ms but violate constraint to only use 32-bit var)
    def reverseBestTime(self, x:int) -> int:
        minus = True if x < 0 else False

        reversed_x = int(str(abs(x))[::-1])

        if reversed_x > (2**31 - 1):
            return 0
        
        return -reversed_x if minus else reversed_x

    # Best memory complexity solution (17MB but violate constraint to only use 32-bit var)
    def reverseBestMemory(self, x:int) -> int:
        temp = abs(x)
        finSum = 0
        while temp!=0:
            r = temp % 10
            finSum = finSum*10 + int(r)
            temp = temp // 10

        finSum = finSum if x>=0 else (-1) * finSum
        if finSum < -2**31 or finSum > 2**31:
            return 0
        return finSum


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(120))
