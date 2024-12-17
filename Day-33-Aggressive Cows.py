class Solution:
    def check(self, stalls, k, mid):
        count = 0
        prev = -1
        for stall in stalls:
            if prev == -1 or stall - prev >= mid:
                count += 1
                prev = stall
        return count >= k

    def aggressiveCows(self, stalls, k):
        stalls.sort()
        
        n = len(stalls)
        lo = 0
        hi = stalls[-1] - stalls[0]
        ans = -1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.check(stalls, k, mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans
