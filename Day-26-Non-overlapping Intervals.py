class Solution:
    def minRemoval(self, intervals):
        # Code here
        deleteCount = 0
        intervals.sort()
        prev = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev:
                deleteCount += 1
                prev = min(prev, intervals[i][1])
            else:
                prev = intervals[i][1]
        
        return deleteCount
