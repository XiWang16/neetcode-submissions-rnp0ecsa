class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort()
        s.sort()
        g_ptr = 0
        s_ptr = 0

        while g_ptr < len(g):
            while s_ptr < len(s) and s[s_ptr] < g[g_ptr]: 
                s_ptr += 1
            if s_ptr == len(s): break
            else: 
                count += 1
                g_ptr += 1
                s_ptr += 1
        
        return count