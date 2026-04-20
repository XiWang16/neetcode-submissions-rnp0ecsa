class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort triplet, check if in ans, then add
        ans = []
        nums.sort()

        # first_ptr,second_ptr,third_ptr = 0,0,0
        for i in range(len(nums)):
            # first_ptr=i
            first = nums[i]
            if first > 0:
                break
            for j in range(i+1,len(nums)):
                # second_ptr
                second = nums[j]
                diff = 0 - first - second
                if diff < 0 and second >= 0:
                    break
                if diff in nums[j+1:]:
                    new = [first, second, diff]
                    if new not in ans:
                        ans.append(new)
        return ans