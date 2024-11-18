class Solution:
    def pushZerosToEnd(self,arr):
        # code here
        lastindex=0
        
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[lastindex],arr[i]=arr[i],arr[lastindex]
                lastindex+=1
