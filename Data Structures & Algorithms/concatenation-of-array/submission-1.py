class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        l = len(nums)
        ans = []
        x = 0
        i = 0

        while x < 2: 
            for z in nums:
                ans.append(z)
            x += 1
        return ans