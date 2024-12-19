class Solution:
    def kthMissing(self, arr, k):
        n = len(arr)
        lo, hi = 0, n - 1
        res = k + n
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] > mid + k:
                res = mid + k
                hi = mid - 1
            else:
                lo = mid + 1
        
        return res
