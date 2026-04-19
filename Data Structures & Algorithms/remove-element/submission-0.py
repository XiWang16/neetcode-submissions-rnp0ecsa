class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums == []:
            return 0
        
        if val <= 50: 
            # check for presence of val and replace in place
            while val in nums:
                nums.remove(val)
        
        return len(nums)