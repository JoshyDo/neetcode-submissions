class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        x = 0

        while x < 2: 
            for z in nums:
                ans.append(z)
            x += 1
        return ans