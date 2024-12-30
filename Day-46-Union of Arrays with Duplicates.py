class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        # code here
        unique_ele = set(a)
        unique_ele.update(b)
        
        return len(unique_ele)
        
