class Solution:
    def maxWater(self, arr):
        # code here
        n= len(arr)
        v=[0]*n
        maxi=0
        
        for i in range(n-1,-1,-1):
            maxi=max(maxi,arr[i])
            v[i]=maxi
            
        maxi=0
        ans=0
        
        for i in range(n):
            maxi=max(maxi,arr[i])
            ans+= max(0,min(maxi,v[i])-arr[i])
        return ans    
            
            
