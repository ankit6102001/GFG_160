class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
    	# code here 
    	n, m = len(mat), len(mat[0])
        lo, hi = 0, n * m - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            row, col = divmod(mid, m)
            
            if mat[row][col] == x:
                return True
            elif mat[row][col] > x:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False
