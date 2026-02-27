"""
Complexity:
- Time  : O(nl^2)
- Space : O(n)
"""
from typing import List
from collections import deque


class Solution:
    # Runtime: 304ms
    # Memory Usage: 20.5MB
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = deque([beginWord])
        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return count
                for i in range(len(word)):
                    for alph in "abcdefghijklmnopqrstuvwxyz":
                        if alph == word[i]:
                            continue
                        new_word = word[:i] + alph + word[i+1:]
                        
                        if new_word in wordSet:
                            queue.append(new_word)
                            wordSet.remove(new_word)
        return 0

    # Best time complexity solution (43ms)
    def ladderLengthBestTime(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        # Bidirectional frontiers
        front = {beginWord}
        back = {endWord}

        # We count number of words in the sequence (beginWord counts as 1)
        steps = 1
        L = len(beginWord)

        # Letters to try for mutation
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        while front and back:
            # Always expand the smaller frontier to reduce work
            if len(front) > len(back):
                front, back = back, front

            next_front = set()

            for word in front:
                # Generate neighbors by mutating each position
                for i in range(L):
                    prefix = word[:i]
                    suffix = word[i+1:]
                    original_char = word[i]

                    for c in alphabet:
                        if c == original_char:
                            continue

                        candidate = prefix + c + suffix

                        # If the candidate is in the opposite frontier, we connected paths
                        if candidate in back:
                            return steps + 1

                        # If candidate is an unvisited dictionary word, add to next frontier
                        if candidate in wordSet:
                            next_front.add(candidate)
                            wordSet.remove(candidate)  # mark visited immediately

            front = next_front
            steps += 1

        return 0

    # Best memory complexity solution (17.57MB)
    def ladderLengthBestMemory(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = []
        ans = 1
        def diff(word1,word2):
            tmp = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    tmp+=1
            if tmp == 1:
                return True
            else:
                return False
        visited = set()
        for word in wordList:
            if diff(word,beginWord):
                queue.append(word)
                visited.add(word)
        # tmp = [beginWord]
        found = False
        while len(queue):
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr == endWord:
                    found = True
                    return ans + 1
                for word in wordList:
                    if word not in visited and diff(word,curr):
                        queue.append(word)
                        visited.add(word)
            ans += 1
        if found:
            return ans
        else:
            return 0


if __name__ == "__main__":
    s = Solution()

    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])) # 5
    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])) # 0
    print(s.ladderLength("hot", "dog", ["hot", "dog"]))
    print(s.ladderLength("hit", "cog", ["hot","dot","tog","cog"]))
    print(s.ladderLength(
        "aaaaa", "uuuuu",
        [
            "aaaaa","waaaa","wbaaa","xaaaa","xbaaa","bbaaa","bbwaa","bbwba","bbxaa",
            "bbxba","bbbba","wbbba","wbbbb","xbbba","xbbbb","cbbbb","cwbbb","cwcbb",
            "cxbbb","cxcbb","cccbb","cccwb","cccwc","cccxb","cccxc","ccccc","wcccc",
            "wdccc","xcccc","xdccc","ddccc","ddwcc","ddwdc","ddxcc","ddxdc","ddddc",
            "wdddc","wdddd","xdddc","xdddd","edddd","ewddd","ewedd","exddd","exedd",
            "eeedd","eeewd","eeewe","eeexd","eeexe","eeeee","weeee","wfeee","xeeee",
            "xfeee","ffeee","ffwee","ffwfe","ffxee","ffxfe","ffffe","wfffe","wffff",
            "xfffe","xffff","gffff","gwfff","gwgff","gxfff","gxgff","gggff","gggwf",
            "gggwg","gggxf","gggxg","ggggg","wgggg","whggg","xgggg","xhggg","hhggg",
            "hhwgg","hhwhg","hhxgg","hhxhg","hhhhg","whhhg","whhhh","xhhhg","xhhhh",
            "ihhhh","iwhhh","iwihh","ixhhh","ixihh","iiihh","iiiwh","iiiwi","iiixh",
            "iiixi","iiiii","wiiii","wjiii","xiiii","xjiii","jjiii","jjwii","jjwji",
            "jjxii","jjxji","jjjji","wjjji","wjjjj","xjjji","xjjjj","kjjjj","kwjjj",
            "kwkjj","kxjjj","kxkjj","kkkjj","kkkwj","kkkwk","kkkxj","kkkxk","kkkkk",
            "wkkkk","wlkkk","xkkkk","xlkkk","llkkk","llwkk","llwlk","llxkk","llxlk",
            "llllk","wlllk","wllll","xlllk","xllll","mllll","mwlll","mwmll","mxlll",
            "mxmll","mmmll","mmmwl","mmmwm","mmmxl","mmmxm","mmmmm","wmmmm","wnmmm",
            "xmmmm","xnmmm","nnmmm","nnwmm","nnwnm","nnxmm","nnxnm","nnnnm","wnnnm",
            "wnnnn","xnnnm","xnnnn","onnnn","ownnn","owonn","oxnnn","oxonn","ooonn",
            "ooown","ooowo","oooxn","oooxo","ooooo","woooo","wpooo","xoooo","xpooo",
            "ppooo","ppwoo","ppwpo","ppxoo","ppxpo","ppppo","wpppo","wpppp","xpppo",
            "xpppp","qpppp","qwppp","qwqpp","qxppp","qxqpp","qqqpp","qqqwp","qqqwq",
            "qqqxp","qqqxq","qqqqq","wqqqq","wrqqq","xqqqq","xrqqq","rrqqq","rrwqq",
            "rrwrq","rrxqq","rrxrq","rrrrq","wrrrq","wrrrr","xrrrq","xrrrr","srrrr",
            "swrrr","swsrr","sxrrr","sxsrr","sssrr","ssswr","sssws","sssxr","sssxs",
            "sssss","wssss","wtsss","xssss","xtsss","ttsss","ttwss","ttwts","ttxss",
            "ttxts","tttts","wttts","wtttt","xttts","xtttt","utttt","uwttt","uwutt",
            "uxttt","uxutt","uuutt","uuuwt","uuuwu","uuuxt","uuuxu","uuuuu","zzzzz",
            "zzzzy","zzzyy","zzyyy","zzyyx","zzyxx","zzxxx","zzxxw","zzxww","zzwww",
            "zzwwv","zzwvv","zzvvv","zzvvu","zzvuu","zzuuu","zzuut","zzutt","zzttt",
            "zztts","zztss","zzsss","zzssr","zzsrr","zzrrr","zzrrq","zzrqq","zzqqq",
            "zzqqp","zzqpp","zzppp","zzppo","zzpoo","zzooo","zzoon","zzonn","zznnn",
            "zznnm","zznmm","zzmmm","zzmml","zzmll","zzlll","zzllk","zzlkk","zzkkk",
            "zzkkj","zzkjj","zzjjj","zzjji","zzjii","zziii","zziih","zzihh","zzhhh",
            "zzhhg","zzhgg","zzggg","zzggf","zzgff","zzfff","zzffe","zzfee","zzeee",
            "zzeed","zzedd","zzddd","zzddc","zzdcc","zzccc","zzccz","azccz","aaccz",
            "aaacz","aaaaz","uuuzu","uuzzu","uzzzu","zzzzu"
        ]
    ))