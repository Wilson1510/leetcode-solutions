"""
Complexity:
- Time  : O(n)
- Space : O(n)
"""
from collections import defaultdict
import bisect


# Runtime: 119ms
# Memory Usage: 20.2MB
class MyCalendarTwo:

    def __init__(self):
        self.schedules = []
        self.overlaps = [] # Menyimpan zona double booking

    def book(self, startTime: int, endTime: int) -> bool:
        # 1. Cek: Apakah menabrak zona double booking yang sudah ada?
        for s, e in self.overlaps:
            if startTime < e and endTime > s:
                return False # Bakal jadi triple booking!
        
        # 2. Jika aman, buat zona double booking baru dari bentrokan dengan schedules
        for s, e in self.schedules:
            if startTime < e and endTime > s:
                # Cari irisan (intersection) untuk disimpan di overlaps
                new_start = max(startTime, s)
                new_end = min(endTime, e)
                self.overlaps.append([new_start, new_end])
        
        # 3. Simpan meeting asli ke schedules
        self.schedules.append([startTime, endTime])
        return True
    

# Best time complexity solution (13ms)
class MyCalendarTwoBestTime:

    def __init__(self):
        self.start = []
        self.end = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        i = bisect.bisect_right(self.start, startTime) #在st之前开始的
        j = bisect.bisect_right(self.end, startTime) # 在st之前结束的
        if i - j > 1: 
            return False
        while i < len(self.start) and self.start[i] < endTime:
            while self.end[j] <= self.start[i]:
                j += 1
            if i - j > 0:
                return False
            i += 1
        bisect.insort(self.start, startTime)
        bisect.insort(self.end, endTime)
        return True

# Best memory complexity solution (17.4MB)
class MyCalendarTwoBestMemory:

    def __init__(self):
        # make a "delta map": an interval [start, end) contributes +1 at start and -1 and end.
        # since the time points run from 0 to 10^9, make this sparse: not an actual list, but a dict.
        self.delta_map = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> bool:
        new_delta_map = self.delta_map.copy()
        new_delta_map[startTime] += 1
        new_delta_map[endTime] -= 1
        curr = 0
        for time in sorted(new_delta_map.keys()):
            delta = new_delta_map[time]
            curr += delta
            if curr >= 3:
                return False
        self.delta_map = new_delta_map
        return True



if __name__ == "__main__":
    myCalender2 = MyCalendarTwo()
    print(myCalender2.book(10, 20)) # True
    print(myCalender2.book(50, 60)) # True
    print(myCalender2.book(10, 40)) # True
    print(myCalender2.book(5, 15)) # False
    print(myCalender2.book(5, 10)) # True
    print(myCalender2.book(25, 55)) # True

    myCalender2 = MyCalendarTwo()
    for startTime, endTime in [
        [24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]
    ]:
        print(myCalender2.book(startTime, endTime))
