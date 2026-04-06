class Solution:
    def findMin(self, nums: List[int]) -> int:
        # list sorted n times - i.e., restored to ascending order
        if nums[0] <= nums[-1]: 
            return nums[0]
        
        s, e = 0, len(nums)

        while e - s > 1:
            mid_idx = s + (e - s) // 2

            if nums[mid_idx] < nums[s]: # min item to the left of the midpoint
                # move end idx left
                e = mid_idx 
            elif nums[mid_idx] > nums[s]: # min item to the right of the midpoint
                # move start idx right
                s = mid_idx
            # note that since all items are unique, we won't have to consider the case where nums[s] == nums[e]

        return nums[e]