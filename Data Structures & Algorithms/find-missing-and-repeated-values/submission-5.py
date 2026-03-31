class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        l = [x for x in range(1, n * n + 1)]
        print(l)
        ans = []
        # traverse all rows
        for row in grid: 
            # traverse all item
            for item in row: 
                if item not in l: 
                    ans.append(item)
                else: 
                    l.remove(item)
        ans.append(l[0])
        return ans
