"""
Complexity:
- Time  : O(4^n)
- Space : O(n)
"""
from typing import List


class Solution:
    # Runtime: 0ms
    # Memory Usage: 19.41MB
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_num = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        results = []
        n = len(digits)

        def backtrack(index, path):
            if len(path) == n:
                results.append("".join(path))
                return
            for ch in phone_num[int(digits[index])]:
                backtrack(index + 1, path + ch)

        backtrack(0, "")
        return results

    # Best time complexity solution (0ms)
    def letterCombinationsBestTime(self, digits: str) -> List[str]:
        lookup = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        return self._combination(lookup, digits, "")

    def _combination(self, lookup: dict, remain: str, store: str):
        if remain == "":
            return [store]
        result = []
        for v in lookup[remain[0]]:
            result += self._combination(lookup, remain[1 :], store+v)
        return result

    # Best memory complexity solution (16.2MB)
    def letterCombinationsBestMemory(self, digits: str) -> List[str]:
        #Time:O(4^n) as each digit represents 4 letters
        #Space:O(n) for recursive call stack
        res = []
        ch_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        def backtrack(comb, remaining_digits):
            if len(remaining_digits) == 0:
                res.append(comb)
            else:
                for ch in ch_map[remaining_digits[0]]:
                    # print(f'ch:{ch}')
                    backtrack(comb+ch, remaining_digits[1:])
        # print(f'res:{res}')
        backtrack('', digits)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(s.letterCombinations("2")) # ["a","b","c"]
    print(s.letterCombinations("")) # []
