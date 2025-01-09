class Solution:
    def subarraySum(self, arr, target):
        # code here
        n=len(arr)
        start=0
        end=0
        total=0
        
        while end<n:
            total+=arr[end]
            
            while total>target:
                total-=arr[start]
                start+=1
                
            if total == target:
                return [start+1,end+1]
                
            end+=1
            
        return [-1]    
            
