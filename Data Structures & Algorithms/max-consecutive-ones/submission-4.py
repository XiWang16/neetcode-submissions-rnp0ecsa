class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        running_len = 0
        for num in nums:
            
            if num == 1:
                running_len += 1
            
            else: 
                if running_len != 0: 
                    if running_len > max_len: 
                        max_len = running_len
                    running_len = 0
            
        
        return max(max_len, running_len)
                

        