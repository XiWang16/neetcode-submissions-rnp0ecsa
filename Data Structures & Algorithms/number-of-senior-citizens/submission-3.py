class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # detail[:11] <- phone number
        # detail[11:12] <- gender
        # detail[12:14] <- age

        ans = 0

        for detail in details:
            print(detail[11:13])
            if int(detail[11:13]) > 60:
                ans += 1

        return ans
        