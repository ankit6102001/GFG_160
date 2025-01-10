class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n=len(arr)
        mp={}
        for i in range(k):
            mp[arr[i]]=mp.get(arr[i],0)+1
        
        ans=[]
        ans.append(len(mp))
        
        for i in range(k,n):
            mp[arr[i]]=mp.get(arr[i],0)+1
            mp[arr[i-k]]-=1
            
            if mp[arr[i-k]]==0:
                del mp[arr[i-k]]
                
            ans.append(len(mp))
        return ans   
