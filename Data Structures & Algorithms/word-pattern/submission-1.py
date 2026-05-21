class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        if len(s_list) != len(pattern): return False

        p_to_s = {}
        s_to_p = {}

        for i in range(len(pattern)):
            if pattern[i] in p_to_s and p_to_s[pattern[i]] != s_list[i]:
                return False
            elif s_list[i] in s_to_p and s_to_p[s_list[i]] != pattern[i]:
                return False
            elif pattern[i] not in p_to_s and s_list[i] not in s_to_p:
                p_to_s[pattern[i]] = s_list[i]
                s_to_p[s_list[i]] = pattern[i]
        
        return True