class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here
        a.sort()
        b.sort()
        
        i, j = 0, 0
        ans = []
        
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                ans.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
            
            while i > 0 and i < len(a) and a[i] == a[i - 1]:
                i += 1

            while j > 0 and j < len(b) and b[j] == b[j - 1]:
                j += 1
        
        return ans
