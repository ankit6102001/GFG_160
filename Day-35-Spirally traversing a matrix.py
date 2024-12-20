class Solution:
    def spirallyTraverse(self, mat):
        ans = []
        top, left = 0, 0
        bottom, right = len(mat) - 1, len(mat[0]) - 1
        
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                ans.append(mat[top][i])
            top += 1
            if top > bottom: break
            
            for i in range(top, bottom + 1):
                ans.append(mat[i][right])
            right -= 1
            if left > right: break
            
            for i in range(right, left - 1, -1):
                ans.append(mat[bottom][i])
            bottom -= 1
            if top > bottom: break
            
            for i in range(bottom, top - 1, -1):
                ans.append(mat[i][left])
            left += 1
        
        return ans
