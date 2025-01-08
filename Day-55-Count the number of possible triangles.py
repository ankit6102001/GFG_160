class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        arr.sort()
        n=len(arr)
        ans=0
        
        for k in range(n-1,1,-1):
            i,j=0,k-1
            while i < j:
                if arr[i] + arr[j]>arr[k]:
                    ans+=(j-i)
                    j-=1
                else:
                    i+=1
        return ans            
