class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        fruit_map = defaultdict(list) 
        # keys: type of fruit, represented by an int
        # values: list of indices of trees that produce the fruit

        for i in range(len(fruits)):
            # if not fruits[i] in fruit_map: 
            #     fruit_map[fruits[i]] = []
            fruit_map[fruits[i]].append(i)
        
        # edge case 1: one type of fruit is produced 
        if len(fruit_map) == 1: return len(fruits)
        # edge case 2: all types of fruit are produced 
        # (Removed edge case 2 as it was incorrect and redundant)

        # general case: multiple types but not all possible types of fruits are produced 
        # logic: put the indices of any two types of fruits together and find the longest sequence 
        max_substr_len = 0
        fruit_type_list = list(fruit_map.keys())

        for i in range(len(fruit_type_list)): 
            fruit_type_1 = fruit_type_list[i]
            for j in range(i + 1, len(fruit_type_list)): 
                fruit_type_2 = fruit_type_list[j]
                # merge the indices 
                l = fruit_map[fruit_type_1] + fruit_map[fruit_type_2]
                l.sort()
                # find longest substr
                length = 1
                for idx in range(len(l) - 1):
                    if l[idx + 1] == l[idx] + 1:
                        length += 1
                    else: 
                        if max_substr_len < length:
                            max_substr_len = length
                        length = 1 # Reset to 1, not 0
                if max_substr_len < length:
                    max_substr_len = length
        
        return max_substr_len