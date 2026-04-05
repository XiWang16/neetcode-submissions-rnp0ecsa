class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        max_len = 1 # base max length
        nums.sort() # O(nlogn) time to sort
        consec_seq = [nums[0]]
        
        for i in range(1, len(nums)):
            if consec_seq[-1] + 1 == nums[i]: # found another num to add to current consec_seq
                consec_seq.append(nums[i])
                if len(consec_seq) > max_len: 
                    max_len = len(consec_seq)
            elif consec_seq[-1] == nums[i]: # found duplicate value
                continue
            else: # consec_seq has stopped; need to restart
                consec_seq = [nums[i]]
        return max_len




        