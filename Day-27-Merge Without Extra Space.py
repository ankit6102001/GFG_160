class Solution:
    def mergeArrays(self, a, b):
        # code here
        combined = a + b
        combined.sort()
        for i in range(len(a)):
            a[i] = combined[i]
        
        for i in range(len(b)):
            b[i] = combined[len(a) + i]
