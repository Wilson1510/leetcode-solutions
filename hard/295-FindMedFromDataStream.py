"""
Complexity:
- Time  : O(log n) for addNum, O(1) for findMedian
- Space : O(n)
"""
from heapq import heappop, heappush


class MedianFinder:
    # Runtime: 170ms
    # Memory Usage: 42.3MB
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int):
        # Gunakan variabel lokal agar akses lebih cepat
        s, l = self.small, self.large
        
        # 1. Tentukan masuk mana dengan 1 operasi push saja
        if not s or num <= -s[0]:
            heappush(s, -num)
        else:
            heappush(l, num)
            
        # 2. Rebalance hanya JIKA diperlukan (selisih > 1 atau l > s)
        if len(s) > len(l) + 1:
            heappush(l, -heappop(s))
        elif len(l) > len(s):
            heappush(s, -heappop(l))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
    

class MedianFinder:
    # Best time complexity solution (26ms)
    def __init__(self):
        self.l = []
        self.r = []

    def addNum(self, num: int) -> None:
        import heapq
        if self.r and num >= self.r[0]:
            heapq.heappush(self.r, num)
        else:
            heapq.heappush(self.l, -num)
        # if self.r:
        #     if num >= self.r[0]:
        #         heapq.heappush(self.r, num)
        #     else:
        #         heapq.heappush(self.l, -num)
        # else:
        #     heapq.heappush(self.l, -num)
        if len(self.l) > len(self.r) + 1:
            x = heapq.heappop(self.l)
            heapq.heappush(self.r, -x)
        elif len(self.r) > len(self.l):
            x = heapq.heappop(self.r)
            heapq.heappush(self.l, -x)

    def findMedian(self) -> float:
        if len(self.l) == len(self.r) + 1:
            return -self.l[0]
        else:
            return (-self.l[0] + self.r[0]) / 2
        

class MedianFinder:
    # Best memory complexity solution (38.5MB)
    def __init__(self):
        self.arr = []
        self.n = 0
        

    def addNum(self, num: int) -> None:
        self.n+=1
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr = sorted(self.arr)
        if self.n % 2 !=0 or self.n==1:
            return self.arr[self.n//2]
        elif self.n==1 : 
            return self.arr[self.n//2]
        return (self.arr[self.n//2] + self.arr[self.n//2 - 1])/2


if __name__ == "__main__":
    medianFinder = MedianFinder()

    medianFinder.addNum(1);    # arr = [1]
    medianFinder.addNum(2);    # arr = [1, 2]
    medianFinder.findMedian(); # return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3);    # arr[1, 2, 3]
    medianFinder.findMedian(); # return 2.0
