class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums)

        while e > s:
            m = s + (e - s) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                e = m
            else:
                s = m + 1

        return -1
        