class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ref = [0, 0, 0] 
        # ref[0] is the buy_idx
        # ref[1] is the sell_idx
        # ref[2] is the max profit

        for i in range(len(prices)):
            buy_idx = i
            for j in range(i, len(prices)):
                sell_idx = j
                profit = prices[j] - prices[i]
                if profit > ref[2]: 
                    ref[0] = buy_idx
                    ref[1] = sell_idx
                    ref[2] = profit

        return ref[2]

        