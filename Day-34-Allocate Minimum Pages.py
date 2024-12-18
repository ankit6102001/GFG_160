class Solution:
    
    def check(self, arr, k, mid):
        number = 1
        pages = 0
        for page in arr:
            if page > mid:
                return False
            if pages + page > mid:
                number += 1
                pages = page
            else:
                pages += page
        return number <= k
    
    def findPages(self, arr, k):
        if len(arr) < k:
            return -1
        lo = max(arr)
        hi = sum(arr)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.check(arr, k, mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
