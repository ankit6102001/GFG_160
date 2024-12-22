class Solution:
    def matSearch(self, mat, x):
        n = len(mat)
        m = len(mat[0]) if n > 0 else 0
        i, j = 0, m - 1
        
        while i < n and j >= 0:
            if mat[i][j] == x:
                return True
            elif mat[i][j] > x:
                j -= 1
            else:
                i += 1
        
        return False
