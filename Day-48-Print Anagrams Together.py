from collections import defaultdict
class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        mp= defaultdict(list)
        for s in arr:
            sort = ''.join(sorted(s))
            mp[sort].append(s)
            
        return list(mp.values())    
         
