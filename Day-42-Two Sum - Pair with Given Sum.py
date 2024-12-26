class Solution:
	def twoSum(self, arr, target):
		# code here
		seen = set()
        for num in arr:
            complement = target - num
            if complement in seen:
                return True
            seen.add(num)
        return False
