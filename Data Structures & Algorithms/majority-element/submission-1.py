from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        ctr=Counter(nums)
        return ctr.most_common()[0][0]