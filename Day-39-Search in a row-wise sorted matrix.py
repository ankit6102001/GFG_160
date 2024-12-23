class Solution:
    def search(self, arr, x):
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == x:
                return True
            elif arr[mid] < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return False

    def searchRowMatrix(self, mat, x):
        n, m = len(mat), len(mat[0])
        for i in range(n):
            if mat[i][0] <= x <= mat[i][m - 1]:
                if self.search(mat[i], x):
                    return True
        return False
