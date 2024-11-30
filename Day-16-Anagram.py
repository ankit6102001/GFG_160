class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #code here
        freq = [0] * 26
        
        for ch in s1:
            freq[ord(ch) - ord('a')] += 1
        
        for ch in s2:
            freq[ord(ch) - ord('a')] -= 1
        
        for count in freq:
            if count != 0:
                return False
        
        return True
