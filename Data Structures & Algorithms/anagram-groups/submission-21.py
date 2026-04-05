class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        # initialize list of anagrams 
        for s in strs: 
            s_sorted = ''.join(sorted(s))
            if s_sorted not in anagrams:
                anagrams[s_sorted] = []
        for s in strs: 
            s_sorted = ''.join(sorted(s))
            anagrams[s_sorted].append(s)

        ans = []
        for l in anagrams.values(): 
            ans.append(l)
        return ans
