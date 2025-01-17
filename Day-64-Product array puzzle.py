class Solution:
    def productExceptSelf(self, arr):
        #code here
        n=len(arr)
        res=[0]*n
        
        product=1
        zero_count=0
        
        for num in arr:
            if num==0:
                zero_count+=1
            else:
                product*=num
        if zero_count > 1:
            return [0]*n
            
        if zero_count ==1:
            for i in range(n):
                if arr[i]==0:
                    res[i]=product
                else:
                    res[i]=0
            return res
            
        for i in range(n):
            res[i]=product//arr[i]
        return res    
            
