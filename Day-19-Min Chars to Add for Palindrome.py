class Solution:
    def minChar(self, s):
        #Write your code here
        rev = s[::-1] 
        combine = s + "*" + rev 
        n = len(combine)
        
        lps = [0] * n
        i = 1
        len_prefix = 0
        
        while i < n:
            if combine[i] == combine[len_prefix]:
                len_prefix += 1
                lps[i] = len_prefix
                i += 1
            elif len_prefix:
                len_prefix = lps[len_prefix - 1]
            else:
                lps[i] = 0
                i += 1
        
        return len(s) - lps[n - 1]
