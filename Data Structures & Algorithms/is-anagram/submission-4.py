class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else: 
            char_indices = set()
            # traverse through all chars in s
            for char in s: 
                # look up each char in t
                if char not in t:
                    return False
                else: 
                    # if found, keep track of the index
                    idx = t.find(char)
                    if idx not in char_indices: 
                        char_indices.add(idx)
                    # if located index alr in set, then look for matches after that index
                    else: 
                        next_idx = t.find(char, idx + 1)
                        # if at any point can't find a match, return false
                        if next_idx == -1: 
                            return False
                        else: 
                            char_indices.add(next_idx)
            # if all chars can be located at unique indices in t, then return true
            return True

        