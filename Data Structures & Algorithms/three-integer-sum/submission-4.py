class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort triplet, check if in ans, then add
        ans = []
        nums.sort()

        for i in range(len(nums)):
            first = nums[i]
            if first > 0:
                break
            if i > 0 and first == nums[i-1]:
                continue
            second_ptr,third_ptr = i + 1, len(nums) -1
       
            while second_ptr<third_ptr:
                threeSum = first + nums[second_ptr] + nums[third_ptr]
                if threeSum == 0:
                    new = [first, nums[second_ptr], nums[third_ptr]]
                    if new not in ans:
                        ans.append(new)
                    third_ptr -= 1
                    second_ptr += 1
                elif threeSum > 0:
                    third_ptr -= 1
                else:
                    second_ptr += 1
        return ans