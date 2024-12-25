class Solution:
    def setMatrixZeroes(self, mat):
        n = len(mat)
        m = len(mat[0])
        flag = 1
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    if i == 0:
                        flag = 0
                    else:
                        mat[i][0] = 0
                        mat[0][j] = 0
        
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
        
        if mat[0][0] == 0:
            for i in range(n):
                mat[i][0] = 0
        
        if flag == 0:
            for j in range(m):
                mat[0][j] = 0
