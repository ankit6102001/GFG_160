class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        start,end,ans=0,0,0
        mp={}
        
        while end< len(s):
            mp[s[end]]=mp.get(s[end],0)+1
            while mp[s[end]]==2:
                mp[s[start]]-=1
                start+=1
                
            ans=max(ans,end-start+1)
            end+=1
        return ans  
