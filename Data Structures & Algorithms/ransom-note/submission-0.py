from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn_ctr = Counter(ransomNote)
        mgz_ctr = Counter(magazine)
        for letter in rn_ctr:
            if letter not in mgz_ctr:
                return False
            else:
                if mgz_ctr[letter] < rn_ctr[letter]:
                    return False
        return True