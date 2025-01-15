from collections import defaultdict
class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefix_sum_indices={}
        curr_sum=0
        longest_length=0
        
        for i in range(len(arr)):
            curr_sum+=arr[i]
            if curr_sum == k:
                longest_length=i+1
                
            if curr_sum-k in prefix_sum_indices:
                longest_length=max(longest_length,i-prefix_sum_indices[curr_sum-k])
                
            if curr_sum not in prefix_sum_indices:
                prefix_sum_indices[curr_sum]=i
                
        return longest_length            
