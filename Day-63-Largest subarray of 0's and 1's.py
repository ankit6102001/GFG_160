class Solution:
    def maxLen(self, arr):
        # code here
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[i]=-1
                
        k =0
        sum_=0
        length=0
        mp={}
        
        for i in range(len(arr)):
            sum_+=arr[i]
            if sum_ == k:
                length=max(length,i+1)
            if sum_ not in mp:
                mp[sum_]=i
            if sum_ - k in mp:
                length=max(length,i-mp[sum_ - k])
                
        return length        
