class Solution:
    def sumClosest(self, arr, target):
        # code here
        arr.sort()
        start,end=0,len(arr)-1
        diff=float('inf')
        ans=[]
        
        while start<end:
            pair_sum=arr[start]+arr[end]
            if abs(target-pair_sum)<diff:
                diff=abs(target-pair_sum)
                ans=[arr[start],arr[end]]
            if pair_sum<target:
                start+=1
            elif pair_sum>target:
                end-=1
            else:
                return ans
        return ans  
