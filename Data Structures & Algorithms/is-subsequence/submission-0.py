class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # s is empty
        if s == "": return True

        # s is NOT empty, but t is empty
        if t == "": return False
        
        # neither s nor t is empty
        start_idx = 0

        for c in s:
            found_in_t = False
            for i in range(start_idx, len(t)):
                if t[i] == c: # found the char!
                    start_idx = i + 1 # to look for the next char in s in t, we start one idx after the idx of the previous char 
                    found_in_t = True
                    break
            if not found_in_t: 
                return False

        return True