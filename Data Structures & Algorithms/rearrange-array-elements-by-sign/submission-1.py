class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # all even indices should be pos and odd neg
        # idea 1: collect all pos & neg numbers in individual arrays and reassemble 
        # more space complexity but just need one pass through the og array?

        pos = []
        neg = []

        for num in nums:
            
            if num > 0:
                pos.append(num)
            else: 
                neg.append(num)
        
        for i in range(len(nums) // 2):
            nums[2 * i] = pos[i]
            nums[2 * i + 1] = neg[i]
        
        return nums
                    
                