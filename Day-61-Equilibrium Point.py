class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        tsum=sum(arr)
        lsum=0
        
        for i in range(len(arr)):
            rsum=tsum-lsum-arr[i]
            if lsum == rsum:
                return i
            lsum+=arr[i]
            
        return -1   
