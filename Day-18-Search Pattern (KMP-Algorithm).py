class Solution:
    def search(self, pat, txt):
        # code here
        result = []
        txt_len = len(txt)
        pat_len = len(pat)
        
        for i in range(txt_len - pat_len + 1):
            if txt[i:i + pat_len] == pat:
                result.append(i)
        
        return result
