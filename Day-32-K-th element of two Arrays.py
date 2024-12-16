class Solution:
    def kthElement(self, a, b, k):
        n, m = len(a), len(b)
        if n > m:
            return self.kthElement(b, a, k)
        
        lo, hi = max(0, k - m), min(n, k)
        
        while lo <= hi:
            mid1 = (lo + hi) // 2
            mid2 = k - mid1
            
            if mid1 == 0:
                l1 = float('-inf')
            else:
                l1 = a[mid1 - 1]
            
            if mid1 == n:
                r1 = float('inf')
            else:
                r1 = a[mid1]
            
            if mid2 == 0:
                l2 = float('-inf')
            else:
                l2 = b[mid2 - 1]
            
            if mid2 == m:
                r2 = float('inf')
            else:
                r2 = b[mid2]
            
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            
            if l1 > r2:
                hi = mid1 - 1
            else:
                lo = mid1 + 1
        
        return 0

