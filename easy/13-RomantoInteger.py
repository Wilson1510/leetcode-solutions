"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""

class Solution:
    # Runtime: 4ms
    # Memory Usage: 19.49MB
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        n = len(s)
        for i in range(n):
            if i + 1 < n and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            else:
                total += roman_to_int[s[i]]
        return total
            

    # Best time complexity solution (0ms)
    def romanToIntBestTime(self, s: str) -> int:
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        total = romans[s[0]]
        i = 1

        while i < len(s):
            # If current value is greater than previous, subtract twice the previous
            if romans[s[i]] > romans[s[i - 1]]:
                total += romans[s[i]] - 2 * romans[s[i - 1]]
            else:
                total += romans[s[i]]
            i += 1

        return total


    # Best memory complexity solution (16.6MB)
    def romanToIntBestMemory(self, s: str) -> int:
        roman_values = self.build_roman_value_map()
        total = 0
        i = 0
        n = len(s)

        while i < n:
            if i == n-1:
                total+=roman_values[s[i]]
                break
            else:
                current_val = roman_values[s[i]]
                next_val = roman_values[s[i+1]]

                if current_val < next_val:
                    total -= current_val
                else:
                    total +=current_val
                i +=1
        return total

    
    def build_roman_value_map(self) -> dict:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        return roman_values

if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))
