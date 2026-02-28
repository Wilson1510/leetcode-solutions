"""
Complexity:
- Time  : O(n)
- Space : O(n)
"""
from bisect import bisect_left
from sortedcontainers import SortedList


# Runtime: 12ms
# Memory Usage: 20.17MB
class MyCalendar:

    def __init__(self):
        self.schedules = []

    def book(self, startTime: int, endTime: int) -> bool:
        # 1. Cari posisi di mana meeting ini seharusnya berada
        # Kita cari berdasarkan startTime
        idx = bisect_left(self.schedules, [startTime, endTime])
        
        # 2. Cek tetangga KIRI (sebelumnya)
        # Apakah meeting sebelumnya selesai SETELAH meeting baru mulai?
        if idx > 0 and self.schedules[idx-1][1] > startTime:
            return False
            
        # 3. Cek tetangga KANAN (sesudahnya)
        # Apakah meeting sesudahnya mulai SEBELUM meeting baru selesai?
        if idx < len(self.schedules) and self.schedules[idx][0] < endTime:
            return False
            
        # Jika lolos kedua cek di atas, aman untuk dipesan!
        self.schedules.insert(idx, [startTime, endTime])
        return True
    

# Best time complexity solution (5ms)
class MyCalendarBestTime:

    def __init__(self):
        self.events = []  # sorted by start time

    def book(self, start: int, end: int) -> bool:
        i = bisect_left(self.events, (start, end))
        
        if i > 0 and self.events[i-1][1] > start:
            return False

        if i < len(self.events) and self.events[i][0] < end:
            return False
        
        self.events.insert(i, (start, end))
        return True

# Best memory complexity solution (17.6MB)
class MyCalendarBestMemory:

    def __init__(self):
        self.calender = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:    
        if len(self.calender) > 0:
            left_idx = self.calender.bisect_left((startTime, endTime))
            if left_idx < len(self.calender):
                curr_start, curr_end = self.calender[left_idx]
                if endTime > curr_start:
                    return False
            if left_idx >= 1:
                curr_start, curr_end = self.calender[left_idx - 1]
                if startTime < curr_end:
                    return False
        self.calender.add((startTime, endTime))
        return True



if __name__ == "__main__":
    myCalender = MyCalendar()
    print(myCalender.book(10, 20)) # True
    print(myCalender.book(15, 25)) # True
    print(myCalender.book(20, 30)) # True

    myCalender = MyCalendar()
    for startTime, endTime in [
        [47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]
    ]:
        print(myCalender.book(startTime, endTime))
