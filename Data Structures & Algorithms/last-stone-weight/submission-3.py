class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # brute force: sort -> smash -> repeat 
        stones.sort()
        while len(stones) > 1:
            last_stone = stones.pop()
            second_to_last_stone = stones.pop()
            if last_stone > second_to_last_stone:
                new_stone = last_stone - second_to_last_stone
                stones.append(new_stone)
                stones.sort()
        if stones != []: 
            return stones[0] 
        else: 
            return 0