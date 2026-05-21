class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans = ""
        distinct = []
        for i in range(len(arr)): 
            if arr[i] not in arr[:i]:
                distinct.append(arr[i])
            else: 
                if arr[i] in distinct: distinct.remove(arr[i])
        if len(distinct) >= k:
            ans = distinct[k - 1]
        return ans
                
        