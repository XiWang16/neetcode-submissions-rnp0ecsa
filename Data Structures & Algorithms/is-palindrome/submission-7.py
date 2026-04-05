import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        translator = str.maketrans('', '', string.punctuation)
        s = s.replace(" ", "").lower().translate(translator)  # remove all white spaces & punctuations and lowercase
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True
        