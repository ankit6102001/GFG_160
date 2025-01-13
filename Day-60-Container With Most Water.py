class Solution:
    def maxWater(self, arr):
        # code here
        ans=0
        l,r=0,len(arr)-1
        
        while l < r:
            ans = max(ans, min(arr[l],arr[r])*(r-l))
            
            if arr[l]<arr[r]:
                l+=1
            else:
                r-=1
                
        return ans     
