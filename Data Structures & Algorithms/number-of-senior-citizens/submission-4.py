class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # detail[:10] <- phone number
        # detail[10:11] <- gender
        # detail[11:13] <- age

        ans = 0

        for detail in details:
            if int(detail[11:13]) > 60:
                ans += 1

        return ans
        