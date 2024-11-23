class Solution:
    def getMinDiff(self, arr, k):
        arr.sort()
        n = len(arr)
        
        if n == 1:
            return 0
        
        ans = arr[-1] - arr[0]
        
        for i in range(1, n):
            if arr[i] >= k:
                max_elem = max(arr[i-1] + k, arr[-1] - k)
                min_elem = min(arr[0] + k, arr[i] - k)
                ans = min(ans, max_elem - min_elem)
        
        return ans
