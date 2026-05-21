from math import sqrt, floor

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        num_take = 0

        while num_take < k:
            gifts.sort() # last pile is the richest
            gifts.append(floor(sqrt(gifts.pop())))
            num_take += 1
        
        return sum(gifts)


        