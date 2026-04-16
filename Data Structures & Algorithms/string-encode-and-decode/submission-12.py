class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        
        strs_length = len(strs)
        if strs_length < 10: res += "0"

        res += str(strs_length)

        running_strs = ""

        for s in strs: 
            s_lenth = len(s)
            if s_lenth < 100: 
                res += "0"
                if s_lenth < 10: 
                    res += "0"
            res += str(s_lenth)
            running_strs += s
        
        res += running_strs
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        strs_length = s[0:2]
        res = []

        length_idx = 2
        strs_idx = length_idx + (int(strs_length) * 3)
        for i in range(int(strs_length)):
            s_length = int(s[length_idx:length_idx + 3])
            res.append(s[strs_idx:strs_idx + s_length])
            length_idx += 3
            strs_idx += s_length
        return res

