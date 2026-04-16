class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        Args:
            words(List[str]): array of strings (non-empty, lowercase English letters only)

        Returns:
            List(str): all words that are a substring of another word in words
        """

        ans = []
        words.sort()
        words.sort(key=len)
        
        for i in range(len(words)):
            cur_word = words[i]
            for j in range(i + 1, len(words)):
                candidate_word = words[j]
                if cur_word in candidate_word:
                    ans.append(cur_word)
                    break
        return ans