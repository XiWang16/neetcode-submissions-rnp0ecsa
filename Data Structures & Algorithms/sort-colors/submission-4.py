from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ctr = Counter(nums)
        print(ctr[0])
        for i in range(len(nums)):
            if i < ctr[0]:
                nums[i] = 0
            elif i < ctr[0] + ctr[1]:
                nums[i] = 1
            else:
                nums[i] = 2
        # nums[:ctr[0]] = 0
        # nums[ctr[0] + 1:ctr[1]] = 1
        # nums[ctr[1] + 1:ctr[2]] = 2
        