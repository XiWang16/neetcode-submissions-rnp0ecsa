class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dynamic sliding window 
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        start, end = 0, 0
        substr = s[start:end] # starts as empty str
        ans = 1

        while end < len(s):
            if s[end] not in substr:
                end += 1
            else:
                while s[start] != s[end]:
                    start += 1
                start += 1
            substr = s[start:end]
            if len(substr) > ans:
                ans = len(substr)
        return ans
            
        