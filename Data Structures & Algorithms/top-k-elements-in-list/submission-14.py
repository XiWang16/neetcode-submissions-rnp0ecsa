class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # two dicts: one mapping nums to their counts, 
        # another mapping counts to nums (for returning final ans)
        num_to_count = defaultdict(int)
        count_to_nums = defaultdict(list)

        for num in nums:
            old_count = num_to_count[num]
            new_count = old_count + 1

            # update num_to_count dict
            num_to_count[num] = new_count

            # update count_to_nums dict
            if new_count not in count_to_nums:
                count_to_nums[new_count] = [num]
            else: 
                count_to_nums[new_count].append(num)
            if old_count in count_to_nums and num in count_to_nums[old_count]:
                count_to_nums[old_count].remove(num)
            
        # return the items in the lists corresponding to the max k keys in count_to_nums
        ans = []
        counts = list(count_to_nums.keys())
        counts.sort()
        i = len(counts) - 1
        while len(ans) < k and i >= 0:
            count = counts[i]
            ans.extend(count_to_nums[count])
            i -= 1
        return ans[:k]