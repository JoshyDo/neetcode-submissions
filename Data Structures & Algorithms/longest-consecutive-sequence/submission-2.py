class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        counter = 1 if nums else 0
        res = 0

        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] == nums[i] + 1:
                counter += 1
                res = max(res, counter)
            elif nums[i] == nums[i + 1]:
                pass
            else:
                counter = 1
                res = max(res, counter)
            i += 1
        return max(counter, res)