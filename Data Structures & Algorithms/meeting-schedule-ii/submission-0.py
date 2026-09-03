"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1
        intervals.sort(key = lambda x :x.start)
        rooms = 1
        for i in range(len(intervals) -1):
            if intervals[i].end > intervals[i+1].start:
                rooms+=1
        return rooms

