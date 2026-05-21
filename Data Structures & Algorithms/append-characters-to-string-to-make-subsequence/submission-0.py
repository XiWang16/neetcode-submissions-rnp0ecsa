class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        i, j = 0, 0 # two pointers, i for t and j for s

        while i < len(t):
            while j < len(s) and t[i] != s[j]: # have not found the curr char in t in s
                j += 1
            # either j == len(s) or we've found the char in t in s
            if j == len(s): # reached the end of s without finding the char in t in s
                return len(t) - i
            else: # the char in t is in s
                i += 1
                j += 1
        
        return 0
                
        