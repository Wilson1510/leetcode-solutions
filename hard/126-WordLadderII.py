"""
Complexity:
- Time  : O(nl^2)
- Space : O(nl)
"""
from typing import List
from collections import defaultdict


class Solution:
    # Runtime: 29ms
    # Memory Usage: 20MB
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        word_set = set(wordList)
        
        # BFS to build parent graph (only keep edges on shortest paths)
        parents = defaultdict(set)
        current_level = {beginWord}
        visited = {beginWord}
        
        while current_level and endWord not in visited:
            next_level = set()
            
            for word in current_level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c != word[i]:
                            next_word = word[:i] + c + word[i+1:]
                            
                            if next_word in word_set and next_word not in visited:
                                next_level.add(next_word)
                                parents[next_word].add(word)
            
            visited.update(next_level)
            current_level = next_level
        
        if endWord not in parents and endWord != beginWord:
            return []
        
        # DFS to build all paths from endWord back to beginWord
        result = []
        
        def dfs(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return
            
            for parent in parents[word]:
                path.append(parent)
                dfs(parent, path)
                path.pop()
        
        dfs(endWord, [endWord])
        return result
            

    # Best time complexity solution (0ms)
    def findLaddersBestTime(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        L = len(beginWord)

        pattern_map = defaultdict(list)
        for word in wordSet:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)

        parents = defaultdict(set)
        level = {beginWord}
        found = False

        while level and not found:
            next_level = set()
            wordSet -= level

            for word in level:
                for i in range(L):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in pattern_map[pattern]:
                        if nei in wordSet:
                            next_level.add(nei)
                            parents[nei].add(word)
                            if nei == endWord:
                                found = True

            level = next_level

        if not found:
            return []

        res = []

        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                dfs(p, path + [p])

        dfs(endWord, [endWord])
        return res

    # Best memory complexity solution (17.3MB)
    def findLaddersBestMemory(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        ws = set(wordList)
        if endWord not in ws:
            return []
        p = defaultdict(list)
        cl = {beginWord}
        found = False
        while cl and not found :
            nl = set()
            for w in cl:
                ws.discard(w)
            for w in cl:
                for i in range(len(w)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        nw = w[:i] + c + w[i+1:]
                        if nw in ws:
                            p[nw].append(w)
                            nl.add(nw)
                            if nw == endWord:
                                found = True
            cl = nl
        result = []
        def backtrack(word,path):
            if word == beginWord:
                result.append(path[::-1])
                return
            for parent in p[word]:
                backtrack(parent ,path + [parent])
        if found:
            backtrack(endWord , [endWord])        
        return result


if __name__ == "__main__":
    s = Solution()

    # [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    print(s.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    print(s.findLadders("hit", "cog", ["hot","dot","dog","lot","log"])) # []
    print(s.findLadders(
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
