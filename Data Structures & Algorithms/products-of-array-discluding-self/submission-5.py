import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums))
        
        prev_product = 1
        for i in range(len(nums)): 
            output[i] = prev_product
            prev_product *= nums[i]

        after_product = 1
        for i in range(len(nums) - 1, -1, -1): # multiply by items to the right
            output[i] *= after_product
            after_product *= nums[i]
        
        return output