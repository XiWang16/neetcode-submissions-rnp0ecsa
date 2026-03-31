class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): 
            dif = target - nums[i]
            try: 
                idx = nums.index(dif, i + 1)
                return [i, idx]
            except ValueError: 
                continue 
        