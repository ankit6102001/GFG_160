from collections import defaultdict
class Solution:
    def subarrayXor(self, arr, k):
        # code here
        mp = defaultdict(int)
        preXor=0
        count=0
        
        for num in arr:
            preXor^=num
            if preXor == k:
                count+=1
            if preXor^k in mp:
                count += mp[preXor^k]
            mp[preXor]+=1
        return count 
