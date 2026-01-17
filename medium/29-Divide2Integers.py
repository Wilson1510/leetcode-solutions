"""
Complexity:
- Time  : O(log n)
- Space : O(1)
"""

class Solution:
    # Runtime: 2ms
    # Memory Usage: 19.39MB
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        is_negative = (dividend < 0) != (divisor < 0)

        dividend = dividend if dividend < 0 else -dividend
        divisor = divisor if divisor < 0 else -divisor

        div_multiple = [divisor]

        while divisor >= -1073741824 and dividend <= (divisor + divisor):
            divisor += divisor
            div_multiple.append(divisor)

        res = 0

        for i in range(len(div_multiple) - 1, -1, -1):
            if dividend <= div_multiple[i]:
                dividend -= div_multiple[i]
                res = res + (1 << i)

        return -res if is_negative else res

    # Best time complexity solution (0ms), violate constraint
    def divideBestTime(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        return int(dividend/divisor)

    # Best memory complexity solution (MB)
    def divideBestMemory(self, dividend: int, divisor: int) -> int:
        # Handle edge case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # Return max value to avoid overflow
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)  # XOR check for different signs
        
        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        # Subtract divisor from dividend using bit shifting
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):  # Shift left (multiply by 2) to find largest multiple
                temp <<= 1
                multiple <<= 1
            
            # Subtract the largest multiple found and add to quotient
            dividend -= temp
            quotient += multiple
        
        # Apply the sign
        if negative:
            quotient = -quotient
        
        # Return the quotient, ensuring it's within 32-bit signed integer limits
        return max(min(quotient, 2**31 - 1), -2**31)


if __name__ == "__main__":
    s = Solution()

    print(s.divide(10, 3))
    print(s.divide(7, -3))
    print(s.divide(2147483647, 1))
