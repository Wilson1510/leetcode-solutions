"""
Complexity:
- Time  : O(n)
- Space : O(n)
"""
from typing import List

class Solution:
    # Runtime: 20ms
    # Memory Usage: 19.86MB
    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        target = {}
        for w in words:
            target[w] = target.get(w, 0) + 1

        word_len = len(words[0])
        n = len(s)

        result = []

        for start in range(word_len):
            left = start
            window = {}
            match = 0

            for right in range(start, n - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in target:
                    window[word] = window.get(word, 0) + 1

                    if window[word] == target[word]:
                        match += 1

                    while window[word] > target[word]:
                        left_word = s[left:left + word_len]
                        if window[left_word] == target[left_word]:
                            match -= 1
                        window[left_word] -= 1
                        left += word_len

                    if match == len(target):
                        result.append(left)

                else:
                    window.clear()
                    match = 0
                    left = right + word_len

        return result

    # Best time complexity solution (56ms)
    def findSubstringBestTime(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        res = []

        sizeEvery = len(words[0])
        biggestWindow = sizeEvery * len(words)
        refs = Counter(words)

        n = len(s)
        for i in range(n - biggestWindow +1):
            l = i
            stopIdx = i + biggestWindow
            currCounter = {}

            while l + sizeEvery <= stopIdx:
                # print(i, l, r)
                currWord = s[l:l+sizeEvery]
                if currWord not in refs:
                    break
                currCounter[currWord] = 1 + currCounter.get(currWord, 0)
                if currCounter[currWord] > refs[currWord]:
                    break
                l += sizeEvery

            if l == stopIdx:
               res.append(i)
        
        return res

    # Best memory complexity solution (17.3MB)
    def findSubstringBestMemory(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        wl = len(words[0])
        wc = len(words)
        tt = wl * wc
        wmap = {}
        for word in words:
            wmap[word] = wmap.get(word, 0) + 1
        res = []
        for i in range(len(s)-tt+1):
            seen = {}
            j = 0
            while j < wc:
                wi=i+j*wl
                word = s[wi:wi+wl]
                if word in wmap:
                    seen[word]=seen.get(word,0)+1
                    if seen[word]>wmap[word]: break
                else: break
                j+=1
            if j==wc:
                res.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    
    print(s.findSubstring("barfoothefoobarman", ["foo","bar"]))
    print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
    print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
