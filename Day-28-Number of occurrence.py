class Solution:
    def countFreq(self, arr, target):
        first, last = -1, -1
        lo, hi = 0, len(arr) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == target:
                first = mid
                hi = mid - 1
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == target:
                last = mid
                lo = mid + 1
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        if last == -1:
            return 0
        return last - first + 1
