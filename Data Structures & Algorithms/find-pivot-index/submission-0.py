class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum = 0
        r_sum = sum(nums[1:])
        i = 0
        while i < len(nums):
            print(l_sum)
            print(r_sum)
            if l_sum == r_sum:
                return i
            l_sum += nums[i]
            if i < len(nums) - 1: r_sum -= nums[i + 1]
            i += 1
        return -1
        