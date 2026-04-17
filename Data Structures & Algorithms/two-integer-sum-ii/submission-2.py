class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2: return [1, 2]

        for i in range(len(numbers)):
            candidate = numbers[i]
            for j in range(i + 1, len(numbers)):
                if numbers[j] + candidate == target: 
                    return [i + 1, j + 1]

        