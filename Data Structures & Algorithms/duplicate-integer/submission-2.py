class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueItems = []
        for num in nums: 
            if num not in uniqueItems: 
                uniqueItems.append(num)
            else: 
                return True
        return False
        