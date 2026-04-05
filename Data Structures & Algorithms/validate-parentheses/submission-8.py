class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = []
        for bracket in s: 
            if bracket in '({[':
                open_brackets.append(bracket)
            else: 
                if open_brackets:
                    test_pair = open_brackets[-1] + bracket
                    if test_pair == '()' or test_pair == '[]' or test_pair == '{}':
                        open_brackets.pop()
                    else: 
                        return False
                else: 
                    return False
        return open_brackets == []