class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if len(arr) < 2:
            return -1  
        
        largest = second_largest = -1
        
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num < largest:
                second_largest = num
        
        return second_largest if second_largest != -1 else -1
