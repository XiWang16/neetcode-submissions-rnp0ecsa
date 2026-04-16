class Solution:
    def scoreOfString(self, s: str) -> int:
        """ Returns the sum of the absolute difference between the ASCII values of adjacent characters

        Args: 
            s(str): a string with characters 

        Returns: 
            int: Sum of all the absolute differences in ASCII values of adjacent characters in s

        """

        sum = 0

        for i in range(len(s) - 1): 
            # get ascii value of the cur and next chars 
            sum += abs(ord(s[i]) - ord(s[i + 1]))

        return sum