class Solution:
    def countSubarrays(self, arr, k):
        # code here
        mp={}
        sum=0
        count=0
        
        for num in arr:
            sum += num
            if sum == k:
                count +=1
            if sum-k in mp:
                count += mp[sum-k]
            if sum in mp:
                mp[sum] +=1
            else:
                mp[sum] = 1
                
        return count  
