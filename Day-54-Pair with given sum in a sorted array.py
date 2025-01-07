class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        ans=0
        i,j=0, len(arr)-1
        
        while i < j:
            curr_sum= arr[i]+arr[j]
            
            if curr_sum<target:
                i+=1
            elif curr_sum > target:
                j-=1
            else:
                ele1, ele2= arr[i],arr[j]
                count1, count2=0,0
                while i <=j and arr[i]==ele1:
                    i+=1
                    count1 += 1
                while i <=j and arr[j]==ele2:
                    j-=1
                    count2 += 1
                if ele1 == ele2:
                    ans+= count1*(count1 - 1) // 2
                else:
                    ans+=count1*count2
        return ans     
