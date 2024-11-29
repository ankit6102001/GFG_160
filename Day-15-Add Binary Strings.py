class Solution:
	def addBinary(self, s1, s2):
		# code here
        s1 = s1[::-1]
        s2 = s2[::-1]
        
        ans = ""
        carry = 0
        i, j = 0, 0
        
        while i < len(s1) and j < len(s2):
            val = carry + int(s1[i]) + int(s2[j])
            carry = val // 2
            val %= 2
            ans += str(val)
            i += 1
            j += 1
        
        while i < len(s1):
            val = carry + int(s1[i])
            carry = val // 2
            val %= 2
            ans += str(val)
            i += 1
        
        while j < len(s2):
            val = carry + int(s2[j])
            carry = val // 2
            val %= 2
            ans += str(val)
            j += 1
        
        while carry:
            val = carry
            carry = val // 2
            val %= 2
            ans += str(val)
        
        ans = ans[::-1]
        
        i = 0
        while i < len(ans) and ans[i] == '0':
            i += 1
        
        if i == 0:
            return ans
        if i == len(ans):
            return "0"
        
        return ans[i:]
