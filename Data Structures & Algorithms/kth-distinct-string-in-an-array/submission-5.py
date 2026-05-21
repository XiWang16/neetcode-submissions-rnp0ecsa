class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans = ""
        
        distinct, seen = set(), set()

        for s in arr: 
            if s in distinct:
                distinct.remove(s)
                seen.add(s)
            if s in seen:
                continue
            distinct.add(s)

        for s in arr: 
            if s in distinct:
                k -= 1
            if k == 0:
                ans = s
                break

        return ans
                
        