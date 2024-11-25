#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
        if not arr:
            return 0
        max_so_far = min_so_far = result = arr[0]
    
        for i in range(1, len(arr)):
            num = arr[i]
    
            if num < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
    
            max_so_far = max(num, max_so_far * num)
            min_so_far = min(num, min_so_far * num)
    
            result = max(result, max_so_far)
    
        return result
