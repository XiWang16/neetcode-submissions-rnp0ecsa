class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # use first word as a reference
        first_str = strs[0]

        common_prefix = ""
        idx = 0

        while idx < len(first_str):
            c = first_str[idx]
            for i in range(len(strs)):
                if strs[i] == "": return ""
                if idx >= len(strs[i]) or strs[i][idx] != c:
                    return common_prefix
            common_prefix += c
            idx += 1
        
        return common_prefix
            
        