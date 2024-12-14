class Solution:
    def search(self,arr,key):
        # Complete this function
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == key:
                return mid
            
            if arr[left] <= arr[mid]:  
                if arr[left] <= key < arr[mid]:  
                    right = mid - 1
                else:  
                    left = mid + 1
            else:  
                if arr[mid] < key <= arr[right]: 
                    left = mid + 1
                else:  
                    right = mid - 1
        
        return -1 
