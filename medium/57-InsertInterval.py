"""
Complexity:
- Time  : O(n)
- Space : O(1)
"""
from typing import List


class Solution:
    # Runtime: 0ms
    # Memory Usage: 21.63MB
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        # 1. Tambahkan yang di kiri (tidak overlap)
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # 2. Gabungkan yang overlap
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        
        # 3. Tambahkan sisanya yang di kanan
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result

    # Best time complexity solution (0ms)
    def insertBestTime(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        res = []
        for i in range(len(intervals)):
            interval = intervals[i]
            
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif newInterval[1] >= interval[0]:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
            else:
                res.append(newInterval)
                return res + intervals[i:]
            
        res.append(newInterval)
        return res

    # Best memory complexity solution (18.6MB)
    def insertBestMemory(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        sol=[]
        start=newInterval[0]
        end=newInterval[1]
        i=0
        while i<len(intervals) and start>intervals[i][1] :
            sol.append(intervals[i])
            i+=1

        while i<len(intervals) and end>=intervals[i][0] :
            start=min(start,intervals[i][0])
            end=max(end,intervals[i][1])
            i+=1
        sol.append([start,end])

        while  i<len(intervals):
            sol.append(intervals[i])
            i+=1
         
        return sol


if __name__ == "__main__":
    s = Solution()

    print(s.insert([[1,3],[6,9]], [2,5])) # [[1,5],[6,9]]
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) # [[1,2],[3,10],[12,16]]
