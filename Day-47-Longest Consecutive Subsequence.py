class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        if not arr:
            return 0
        nums = set(arr)
        longest_streak=0
        
        for num in nums:
            if num -1 not in nums:
                curr_num = num
                curr_streak= 1
                
                while curr_num + 1 in nums:
                    curr_num+=1
                    curr_streak+=1
                    
                longest_streak = max(longest_streak, curr_streak)
                
        return longest_streak     
