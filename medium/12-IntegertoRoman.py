"""
Complexity:
- Time  : O(1)
- Space : O(1)
"""

class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.24MB
    def intToRoman(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return (
            thousands[num // 1000]
            + hundreds[num % 1000 // 100]
            + tens[num % 100 // 10]
            + ones[num % 10]
        )

    # Best time complexity solution (0ms)
    def intToRomanBestTime(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return (
            thousands[num // 1000]
            + hundreds[num % 1000 // 100]
            + tens[num % 100 // 10]
            + ones[num % 10]
        )

    # Best memory complexity solution (16.6MB)
    def intToRomanBestMemory(self, num: int) -> str:
        roman = []
        digits = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        for val, symbol in digits:
            count, num = divmod(num, val)
            roman.append(count*symbol)
        
        return ''.join(roman)


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(3749)) # MMMDCCXLIX
    print(s.intToRoman(58)) # LVIII
    print(s.intToRoman(1994)) # MCMXCIV
    print(s.intToRoman(4)) # IV
    print(s.intToRoman(9)) # IX
    print(s.intToRoman(101)) # CI
